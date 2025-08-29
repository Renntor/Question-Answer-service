from api.mixins import CreateListRetrieveDestroyMixin, CreateRetrieveDestroyMixin
from api.qa.serializers import QuestionSerializer, RetrieveDestroyAnswerSerializer, RetrieveQuestionSerializer, \
    AnswerSerializer
from api.qa.services import AnswerServices
from qa_app.models import Question, Answer


class QuestionViewSet(CreateListRetrieveDestroyMixin):
    queryset = Question.objects.all()

    def get_serializer_class(self):
        match self.action:
            case 'retrieve':
                return RetrieveQuestionSerializer
            case _:
                return QuestionSerializer


class AnswerViewSet(CreateRetrieveDestroyMixin):
    queryset = Answer.objects.all()

    def get_serializer_class(self):
        match self.action:
            case 'create':
                return AnswerSerializer
            case _:
                return RetrieveDestroyAnswerSerializer

    def perform_create(self, serializer):
        question = AnswerServices.checking_question(self.kwargs.get('pk'))
        serializer.save(question=question)
