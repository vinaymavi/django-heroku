from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Question

# Create your views here.
def index(request):	
	question_list = Question.objects.order_by('-pub_date')[:5]	
	template = loader.get_template("polls/index.html")
	context = RequestContext(request,{'question_list':question_list})
	return HttpResponse(template.render(context))

def detail(request,question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist, e:
		raise Http404("Question does not exist.")
	return render(request,'polls/detail.html',{"question":question})

def results(request,question_id):
	return HttpResponse("Looking for question %s results" % question_id)

def vote(request,question_id):
	return HttpResponse("You are voting on question %s" % question_id)



