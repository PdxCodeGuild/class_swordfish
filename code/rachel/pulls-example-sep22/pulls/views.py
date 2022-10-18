from django.http import HttpResponse #what will be returned after running function

from .models import Question, Choice
from django.shortcuts import render, get_object_or_404

def index(request): #always first function in view
    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # output = '<ul/><li>' + '<li/><li>'.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    return render(request, 'pulls/index.html', {'latest_question_list': latest_question_list})
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pulls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse(f"Your're looking at the results of question number {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"Your're voting on question number {question_id}.")