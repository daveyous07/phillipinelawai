"""
Test Simulation Service - Generates practice questions and evaluates answers.
"""
import re
from typing import List, Optional

from app.config import settings
from app.services.gemini_client import generate_content_async


# Expected LLM output format for questions
QUESTION_FORMAT = """
Generate exactly ONE multiple-choice question about Philippine law.
Format strictly as:
QUESTION: [your question]
A) [option A]
B) [option B]
C) [option C]
D) [option D]
ANSWER: [A, B, C, or D]
SOURCE: [constitution/article/section cited]
"""


def parse_question_response(raw: str) -> Optional[dict]:
    """
    Parse LLM-generated question into structured format.
    Returns dict with question, options, correct_answer, source or None if parse fails.
    """
    out = {
        "question": "",
        "options": {"A": "", "B": "", "C": "", "D": ""},
        "correct_answer": "",
        "source": "",
    }
    # Extract QUESTION
    q_match = re.search(r"QUESTION:\s*(.+?)(?=A\)|$)", raw, re.DOTALL | re.I)
    if q_match:
        out["question"] = q_match.group(1).strip()

    for opt in "ABCD":
        opt_match = re.search(
            rf"{opt}\)\s*(.+?)(?=[A-D]\)|ANSWER:|$)",
            raw,
            re.DOTALL | re.I,
        )
        if opt_match:
            out["options"][opt] = opt_match.group(1).strip()

    ans_match = re.search(r"ANSWER:\s*([A-D])", raw, re.I)
    if ans_match:
        out["correct_answer"] = ans_match.group(1).upper()

    src_match = re.search(r"SOURCE:\s*(.+)", raw, re.I)
    if src_match:
        out["source"] = src_match.group(1).strip()

    if not out["question"] or not out["correct_answer"]:
        return None
    return out


class TestService:
    """Generates and evaluates practice test questions."""

    async def generate_question(
        self,
        topic: Optional[str] = None,
        difficulty: str = "moderate",
    ) -> dict:
        """
        Generate a single practice question via LLM.
        topic: optional focus (e.g., "Bill of Rights", "Civil Code")
        difficulty: easy, moderate, hard
        """
        prompt = f"""Generate a {difficulty} multiple-choice question for Philippine law students.
{f'Focus on: {topic}.' if topic else 'Cover any area of Philippine Constitution or laws.'}

{QUESTION_FORMAT}"""

        messages = [
            {"role": "system", "content": "You are a Philippine law exam writer. Output strictly in the required format."},
            {"role": "user", "content": prompt},
        ]
        try:
            if settings.llm_backend.strip().lower() == "ollama":
                from ollama import AsyncClient

                client = AsyncClient(host=settings.ollama_base_url)
                resp = await client.chat(model=settings.ollama_model, messages=messages)
                raw = resp.message.content or ""
            else:
                raw = await generate_content_async(
                    settings.gemini_model,
                    messages,
                    api_key=settings.google_api_key or None,
                )
            parsed = parse_question_response(raw)
            if parsed:
                return {"success": True, "question": parsed}
            return {"success": False, "raw": raw, "error": "Could not parse question"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    async def evaluate_answer(
        self,
        question_data: dict,
        user_answer: str,
    ) -> dict:
        """
        Evaluate user's answer. Returns correctness and feedback.
        """
        correct = question_data.get("correct_answer", "").upper()
        user = user_answer.strip().upper()
        if len(user) == 1:
            user = user[0]
        else:
            # Handle "A." or "option A" etc.
            m = re.search(r"[A-D]", user)
            user = m.group(0) if m else user

        is_correct = user == correct
        feedback = (
            f"Correct! {question_data.get('source', '')}"
            if is_correct
            else f"Incorrect. The correct answer is {correct}. {question_data.get('source', '')}"
        )
        return {
            "correct": is_correct,
            "user_answer": user,
            "correct_answer": correct,
            "feedback": feedback,
        }


test_service = TestService()
