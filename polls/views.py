from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from polls.serializers import ChoiceSerializer



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
    'latest_question_list': latest_question_list,
    }    
    return HttpResponse(request)

def index_t(request):
    return HttpResponse("Hello, 123")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse(request)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = ChoiceSerializer

    def get_object(self):
        return get_object_or_404(Choice, pk=self.kwargs.get('question_id'))
