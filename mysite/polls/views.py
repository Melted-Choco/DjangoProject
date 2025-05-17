from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World. You're at the polls index.")

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
