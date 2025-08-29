import pytest
from rest_framework.test import APIClient
from rest_framework import status
from qa_app.models import Question, Answer


@pytest.mark.django_db(transaction=True)
class Test01QuestionAPI:
    URL_LIST_CREATE = '/api/questions/'
    URL_RETRIEVE_DELETE = '/api/questions/{id}/'

    def setup_method(self):
        self.client = APIClient()

    def test_create_question(self, first_question_data):
        """
        Проверка на возможность создать вопрос.
        """
        response = self.client.post(self.URL_LIST_CREATE, first_question_data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert Question.objects.count() == 1

    def test_list_question(self, ready_question, ready_question_two):
        """
        Проверка на возможность получить список всех вопросов.
        """
        response = self.client.get(self.URL_LIST_CREATE)
        assert response.status_code == status.HTTP_200_OK
        assert Question.objects.count() == 2
        assert len(response.data) == Question.objects.count()

    def test_delete_question(self, question_id_for_args, ready_question_two):
        """
        Проверка на возможность удалить вопрос.
        """
        response = self.client.delete(self.URL_RETRIEVE_DELETE.format(id=question_id_for_args))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Question.objects.count() == 1

    def test_retrieve_question(self, question_id_for_args, ready_answer):
        """
        Проверка на возможность получить вопрос и ответы на этот вопрос.
        """
        response = self.client.get(self.URL_RETRIEVE_DELETE.format(id=question_id_for_args))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['answers']) == Answer.objects.count()
