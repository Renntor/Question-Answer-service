from  django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.qa.view import QuestionViewSet, AnswerViewSet

app_name = 'api'

router = DefaultRouter()
router.register('questions', QuestionViewSet, basename='questions')


urlpatterns = [
    path('', include(router.urls)),
    path(
        'questions/<int:pk>/answers/',
        AnswerViewSet.as_view({'post' : 'create'}),
        name='answer-create'
    ),
    path(
        'answers/<int:pk>/',
        AnswerViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}),
        name='answer-retrieve-destroy'
    )

]