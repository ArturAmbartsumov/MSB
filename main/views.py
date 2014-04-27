from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from main.models import *

def index(request):
	articleList = get_list_or_404(ArticleDescriptions)
	return render(request, 'main/index.html', {'articleList': articleList})

def article(request, article):
	article = get_object_or_404(Articles, short_name = article)
	return render(request, 'main/' + article.template, {'article': article})

def articles(request):
	articleList = get_list_or_404(ArticleDescriptions)
	return render(request, 'main/articles.html', {'articleList': articleList})

def department(request, department):
	department = get_object_or_404(Departments, short_name = department)
	return render(request, 'main/' + department.template, {'department': department})

def project(request, project):
	project = get_object_or_404(Projects, short_name = project)
	return render(request, 'main/' + project.template, {'project': project})

def projects(request):
	projectList = get_list_or_404(Projects)
	return render(request, 'main/projects.html', {'projectList': projectList})