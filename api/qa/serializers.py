from rest_framework import serializers

from qa_app.constants import AnswerConstants, QuestionConstants
from qa_app.models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с ответами
    """

    text = serializers.CharField(
        min_length=AnswerConstants.Length.MIN_LENGTH_TEXT
    )

    class Meta:
        model = Answer
        fields = ('id', 'text', 'user_id', 'created_at')


class RetrieveDestroyAnswerSerializer(AnswerSerializer):
    """
    Сериализатор для работы с ответами
    """

    class Meta:
        model = Answer
        fields = AnswerSerializer.Meta.fields + (
            'question',
        )


class QuestionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с вопросами
    """
    text = serializers.CharField(
        min_length=QuestionConstants.Length.MIN_LENGTH_TEXT
    )

    class Meta:
        model = Question
        fields = ('id', 'text', 'created_at')


class RetrieveQuestionSerializer(QuestionSerializer):
    """
    Сериализатор для вывода вопроса и всех ответов на него
    """
    answers = RetrieveDestroyAnswerSerializer(many=True, read_only=True)

    class Meta:
        fields = QuestionSerializer.Meta.fields + (
            'answers',
        )
        model = Question
