from django.http import Http404

from qa_app.models import Question


class AnswerServices:

    @staticmethod
    def checking_question(pk: str) -> Question:
        """Проверка на существование вопроса."""
        question = Question.objects.filter(pk=pk)
        if not Question.objects.filter(pk=pk):
            raise Http404
        return question.first()
