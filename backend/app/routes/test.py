"""
Test Simulation API - Generate questions and evaluate answers.
"""
from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

from app.services.test_service import test_service

router = APIRouter()


class GenerateRequest(BaseModel):
    topic: Optional[str] = None
    difficulty: str = "moderate"


class SubmitRequest(BaseModel):
    question: dict
    answer: str


@router.post("/generate")
async def generate_question(request: GenerateRequest):
    """Generate a practice multiple-choice question."""
    result = await test_service.generate_question(
        topic=request.topic,
        difficulty=request.difficulty,
    )
    return result


@router.post("/submit")
async def submit_answer(request: SubmitRequest):
    """Submit answer and get feedback."""
    return await test_service.evaluate_answer(
        question_data=request.question,
        user_answer=request.answer,
    )
