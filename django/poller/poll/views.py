from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.mail import send_mail
# Create your views here.
from .models import Question,Choice
def homepage(request):
    context={
        “title”:”Home Page”,
    }
    return render(request, “home.html”,context)
def ownerpage(request):
    context={
        “title”:”Owner Page”,
    }
    return render(request, “owner.html”,context)
def contactpage(request):
    if request.method==”POST”:
        messagename=request.POST[‘fullname’]
        email=request.POST[‘email’]
        message=request.POST[‘content’]
        send_mail(
            ‘surveyEarth’, #subject
            message,  #message
            email, # from email
            [‘jishnusaurav@gmail.com’],  #to email
        )
        return render(request,’contact.html’,{‘messagename’:messagename})
    else:
        return render(request, “contact.html”,{})
def index(request):
latest_question_list=Question.objects.order_by(‘-pub_date’)[:5]
    context={‘latest_question_list’:latest_question_list}
    return render(request,’polls/index.html’,context)
def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404(“Question does not exist”)
    return render(request,’polls/detail.html’,{‘question’:question})
def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
return render(request,’polls/results.html’,{‘question’:question})
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST[‘choice’])
    except (KeyError, Choice.DoesNotExist):
        return render(request, ‘polls/detail.html’, {
            ‘question’: question,
            ‘error_message’: “You didn’t select a choice.”,
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse(‘polls:results’, args=(question.id,)))
def resultsData(request, obj):
    votedata = []
    question = Question.objects.get(id=obj)
    votes = question.choice_set.all()
    for i in votes:
        votedata.append({i.choice_text:i.votes})
    print(votedata)
