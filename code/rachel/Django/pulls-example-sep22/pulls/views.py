# from django.http import HttpResponse #what will be returned after running function

from .models import Question, Choice

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from django.urls import reverse

def index(request): #always first function in view
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10] #lte = later than or equal to
    # output = ', '.join([q.question_text for q in latest_question_list])
    # output = '<ul/><li>' + '<li/><li>'.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    return render(request, 'pulls/index.html', {'latest_question_list': latest_question_list})
    
def detail(request, question_id):
    question = get_object_or_404(Question.objects.filter(pub_date__lte=timezone.now()), pk=question_id)
    return render(request, 'pulls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question.objects.filter(pub_date__lte=timezone.now()), pk=question_id)
    return render(request, 'pulls/results.html', {'question': question})

def vote(request, question_id):
    # return HttpResponse(f"Your're voting on question number {question_id}.")
    question = get_object_or_404(Question.objects.filter(pub_date__lte=timezone.now()), pk=question_id)
    try:
        choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'pulls/detail.html', {
            'question': question,
            'error_message': "Please select a valid choice." 
        })
    choice.votes += 1
    choice.save()
    return HttpResponseRedirect(reverse('pulls:results', args=(question.id,)))