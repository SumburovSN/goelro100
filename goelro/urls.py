from django.urls import path
from . import views

urlpatterns = [
    path('i', views.index),
    path('1', views.show),
    path('form-handler/', views.form_handler),
    path('', views.base),
    path('quizzes', views.quizzes),
    path('quiz/<int:number>', views.quiz, name='number'),
    # path('quizzes', views.QuizFormView.as_view()),
    path('audios', views.audios),
    path('audio/<int:number>', views.audio, name='number'),
    path('references', views.references),
    path('test1/check', views.test1_check),
    path('article/<int:number>', views.article, name='number'),
]
