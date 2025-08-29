import pytest

from qa_app.models import Question


@pytest.fixture
def first_question_data() -> dict:
    return {
        'text': 'Вопрос 1.'
    }

@pytest.fixture
def second_question_data() -> dict:
    return {
        'text': 'Вопрос 2.'
    }

@pytest.fixture
def ready_question() -> Question:
    return Question.objects.create(
        text='Вопрос готовый'
    )

@pytest.fixture
def question_id_for_args(ready_question: Question) -> int:
    return ready_question.id


@pytest.fixture
def ready_question_two() -> Question:
    return Question.objects.create(
        text='Вопрос готовый два'
    )