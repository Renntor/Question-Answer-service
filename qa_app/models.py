from django.db import models

from qa_app.constants import QuestionConstants


class Question(models.Model):
    text = models.CharField(
        max_length=QuestionConstants.Length.MAX_LENGTH_TEXT,
        verbose_name='Вопрос',
        help_text='Текст вопроса',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания',
        help_text='Время создания вопроса',
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f'Вопрос: {self.text}.\n Создан: {self.created_at}'


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        related_name='answers',
        on_delete=models.CASCADE,
        verbose_name='Вопрос',
        help_text='Укажите вопрос, к которому относится ответ',
    )
    user_id = models.UUIDField(
        verbose_name='UUID',
        help_text='UUID пользователя',
    )
    text = models.TextField(
        verbose_name='Ответ',
        help_text='Ответ пользователя на вопрос',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания',
        help_text='Время создания ответа пользователя',
    )

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return (
            f'Вопрос: {self.question.text}.\n'
            f'Ответ: {self.text}.\n'
            f'Создан: {self.created_at}'
        )
