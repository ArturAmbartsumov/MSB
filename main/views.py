from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from main.models import *

def index(request):
	articleList = get_list_or_404(ArticleDescriptions)
	return render(request, 'main/index.html', {'articleList': articleList})

def article(request, article):
	article = get_object_or_404(Articles, short_name = article)
	return render(request, 'main/index.html', {'article': article})

def department(request, department):
	return HttpResponse("You're looking at department %s." % department)

def project(request, department, project):
	message = "You're looking at department %s " % department
	message += "and project %s." % project
	return HttpResponse(message)
