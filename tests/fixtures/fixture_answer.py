import pytest

from qa_app.models import Answer, Question


@pytest.fixture
def first_answer_data() -> dict:
    return {
        'user_id': '550e8400-e29b-41d4-a716-446655440000',
        'text': 'Ответ на вопрос.'
    }

@pytest.fixture
def second_answer_data() -> dict:
    return {
        'user_id': '550e8400-e29b-41d4-a716-446655440000',
        'text': 'Ответ на вопрос.'
    }

@pytest.fixture
def ready_answer(ready_question: Question) -> Answer:
    return Answer.objects.create(
        question=ready_question,
        user_id='440e8400-e29b-41d4-a716-446655440000',
        text='Answer'
    )

@pytest.fixture
def ready_answer_two(ready_question: Question) -> Answer:
    return Answer.objects.create(
        question=ready_question,
        user_id='550e8400-e29b-41d4-a716-446655440000',
        text='Answer_two'
    )

@pytest.fixture
def answer_id_for_args(ready_answer: Answer) -> int:
    return ready_answer.id
