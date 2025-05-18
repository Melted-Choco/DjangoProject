from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    # Receive data in the latest order based on pub_date
    latest_question_list = Question.objects.order_by('-pub_date')[:5] # only Top 5
    # Load 'index.html'
    template = loader.get_template('polls/index.html')
    # Save the Question data in the 'context' dictionary
    context = {
        'latest_question_list' : latest_question_list,
    }
    # Send the content of 'context'
    return HttpResponse(template.render(context, request))

# Show question_text
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

# Show the result of Question
def results(request, question_id):
    response = "You're looking at the results of quesiton %s."
    return HttpResponse(response % question_id)

# Function of Voting
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
