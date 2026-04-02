"""
Test Service - Uses simple LLM. No async.
"""
import re
from typing import Optional

from app.services.llm_simple import chat_for_test

QUESTION_FORMAT = """
Generate exactly ONE multiple-choice question about Philippine law, Shariah law, or landmark cases.
Cover topics: Constitutional Law, Criminal Law, Civil Law, Obligations and Contracts,
Labor Law, Evidence, Remedies, Commercial Law, Taxation, Administrative Law, Election Laws,
Local Government, Family Law, Succession, Torts and Damages, Shariah/Islamic Law.
When suitable, include questions on Supreme Court cases and doctrines (e.g., Ang Tibay, Miranda,
Hacienda Luisita, piercing the corporate veil, quasi-delict, res judicata).
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
    out = {"question": "", "options": {"A": "", "B": "", "C": "", "D": ""}, "correct_answer": "", "source": ""}
    q_match = re.search(r"QUESTION:\s*(.+?)(?=A\)|$)", raw, re.DOTALL | re.I)
    if q_match:
        out["question"] = q_match.group(1).strip()
    for opt in "ABCD":
        opt_match = re.search(rf"{opt}\)\s*(.+?)(?=[A-D]\)|ANSWER:|$)", raw, re.DOTALL | re.I)
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


def generate_question(topic: Optional[str] = None, difficulty: str = "moderate") -> dict:
    prompt = f"""Generate a {difficulty} multiple-choice question for Philippine law students.
{f'Focus on: {topic}.' if topic else 'Cover any area of Philippine Constitution or laws.'}

{QUESTION_FORMAT}"""
    system = (
        "You are a Philippine law exam writer. Generate questions based ONLY on the Constitution, "
        "statutes (Civil Code, RPC, Labor Code, etc.), and Supreme Court jurisprudence. Do NOT invent "
        "article numbers, provisions, or case names. Use real law and cases. Output strictly in the required format."
    )
    raw = chat_for_test(prompt, system=system)
    parsed = parse_question_response(raw)
    if parsed:
        return {"success": True, "question": parsed}
    return {"success": False, "raw": raw, "error": "Could not parse question"}


def evaluate_answer(question_data: dict, user_answer: str) -> dict:
    correct = question_data.get("correct_answer", "").upper()
    user = user_answer.strip().upper()
    if len(user) == 1:
        user = user[0]
    else:
        m = re.search(r"[A-D]", user)
        user = m.group(0) if m else user
    is_correct = user == correct
    feedback = (
        f"Correct! {question_data.get('source', '')}"
        if is_correct
        else f"Incorrect. The correct answer is {correct}. {question_data.get('source', '')}"
    )
    return {"correct": is_correct, "user_answer": user, "correct_answer": correct, "feedback": feedback}
