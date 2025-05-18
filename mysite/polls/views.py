from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question

def index(request):
    # Receive data in the latest order based on pub_date
    latest_question_list = Question.objects.order_by('-pub_date')[:5] # only Top 5
    # Save the Question data in the 'context' dictionary
    context = {
        'latest_question_list' : latest_question_list,
    }
    # Render() : Wrapping function
    # Load 'index.html' & Send the content of 'context'
    return render(request, 'polls/index.html', context)

# Show question_text
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exists")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# Show the result of Question
def results(request, question_id):
    response = "You're looking at the results of quesiton %s."
    return HttpResponse(response % question_id)

# Function of Voting
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
