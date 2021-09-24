INSTALL:


pip3 install django

django-admin startproject poller

python manage.py runserver

python manage.py startapp poll

cd poller

mkdir templates

INSTALLED_APPS = [
    ‘polls.apps.PollsConfig’,
    ‘django.contrib.admin’,
    ‘django.contrib.auth’,
    ‘django.contrib.contenttypes’,
    ‘django.contrib.sessions’,
    ‘django.contrib.messages’,
    ‘django.contrib.staticfiles’,
    ‘polls’,
]


then next vi poller/urls.py

path(‘polls/’, include(‘polls.urls’)),
    path(‘admin/’, admin.site.urls),
    url(r’^$’,homepage,name=’home’),]

Then go One step above this foleder back to poll

vi poll/admin.py

from polls.models import Question,Choice
admin.site.site_header=”surveyEarth Admin”
admin.site.site_title=”surveyEarth Admin Page”
admin.site.index_title=”Welcome to the surveyEarth Admin Page”
class ChoiceInLine(admin.TabularInline):
    model=Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[(None,{‘fields’:[‘question_text’]}),
    (‘Date Information’,{‘fields’:[‘pub_date’],’classes’:[‘collapse’]}),]
    inlines=[ChoiceInLine]
admin.site.register(Question,QuestionAdmin)


then vi poll/models.py

class Question(models.Model):
question_text=models.CharField(max_length=200)
pub_date=models.DateTimeField(‘date published’)
def __str__(self):
return self.question_text
class Choice(models.Model):
question=models.ForeignKey(Question, on_delete=models.CASCADE)
choice_text=models.CharField(max_length=200)
votes=models.IntegerField(default=0)
def __str__(self):
return self.choice_text


Then go back to poll/urls.py

vi the above file

from . import views
app_name=’polls’
urlpatterns=[
    path(‘’,views.index, name=’index’),
    path(‘<int:question_id>/’, views.detail, name=’detail’),
    path(‘<int:question_id>/results/’, views.results, name=’results’),
    path(‘<int:question_id>/vote/’,views.vote,name=’vote’),
    path(‘resultsdata/<str:obj>/’, views.resultsData, name=”resultsdata”),
]

Then go to poll/views.py

vi the above file

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



vi poll/templates/base.html

<!DOCTYPE html>
<html lang=”en”>
<head>
<meta charset=”UTF-8”>
<meta name=”viewport” content=”width=device-width, initial-scale=1.0”>
<meta http-equiv=”X-UA-Compatible” content=”ie=edge”>
<link
rel=”stylesheet”
href=”https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css”
integrity=”sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T”
crossorigin=”anonymous”
/>
<title>surveyEarth {% block title %}{% endblock %}</title>
</head>
<body>
{% include ‘navbar.html’ with brand_name=’vote’ %}
<div class=”container”>
<div class=”row”>
<div class=”col-md-6 m-auto”>
{% block content %}{% endblock %}
</div>
</div>
</div>
</body>
</html> 


vi poll/templates/home.html

{% extends ‘base.html’ %}
{% block content %}
<div style=”background-color: #404040; width: 500px; height: 200px; color: white; margin: 200px 50px 100px 50px;”>
<h1>Welcome!!</h1>
<br>
<h3>Click on start to start the survey</h3>
<center><a class = “btn btn-success “ href=”{% url ‘polls:index’ %}”>Start</a></center>
</div>
{% endblock %}





TROUBLESHOOT:


Python3 manage.py makemigration
Python3 manage.py migrate
Python3 manage.py runserver
