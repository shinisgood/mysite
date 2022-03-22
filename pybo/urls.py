from django.urls import path

from .views import base_views, answer_views, question_views

app_name = 'pybo'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('question/create/', question_views.question_create, name='question_create'),
]