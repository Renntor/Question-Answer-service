import pytest
from rest_framework.test import APIClient
from rest_framework import status
from qa_app.models import Answer


@pytest.mark.django_db(transaction=True)
class Test02AnswerAPI:
    URL_RETRIEVE_DELETE = '/api/answers/{id}/'
    URL_CREATE = '/api/questions/{id}/answers/'

    def setup_method(self):
        self.client = APIClient()

    def test_create_answers(self, question_id_for_args, first_answer_data):
        """
        Проверка на возможность создать ответ.
        """
        response = self.client.post(self.URL_CREATE.format(id=question_id_for_args), first_answer_data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert Answer.objects.count() == 1

    def test_delete_answers(self, answer_id_for_args):
        """
        Проверка на возможность удалить ответ.
        """
        response = self.client.delete(self.URL_RETRIEVE_DELETE.format(id=answer_id_for_args))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Answer.objects.count() == 0

    def test_retrieve_answers(self, answer_id_for_args):
        """
        Проверка на возможность получить ответ.
        """
        response = self.client.get(self.URL_RETRIEVE_DELETE.format(id=answer_id_for_args))
        assert response.status_code == status.HTTP_200_OK
        assert Answer.objects.count() == 1
