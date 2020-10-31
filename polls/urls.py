from django.test import TestCase

# Create your tests here.

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_t/', views.index_t, name='index_t'),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('choice/', views.ChoiceList.as_view(), name='list'),
    path('choice/<int:question_id>/', views.ChoiceDetail.as_view(), name='details'),
]