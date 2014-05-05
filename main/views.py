from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from main.models import *

def index(request):
	#articleList = get_list_or_404(ArticleDescriptions)
	#return render(request, 'main/index.html', {'articleList': articleList})
	return render(request, 'main/index.html')

def article(request, article):
	#article = get_object_or_404(Articles, short_name = article)
	#return render(request, 'main/' + article.template, {'article': article})
	return render(request, 'main/article.html')

def articleList(request):
	#articleList = get_list_or_404(ArticleDescriptions)
	#return render(request, 'main/articles.html', {'articleList': articleList})
	return render(request, 'main/articles.html')

def department(request, department):
	#department = get_object_or_404(Departments, short_name = department)
	#return render(request, 'main/' + department.template, {'department': department})
	return render(request, 'main/department.html')

def project(request, project):
	#project = get_object_or_404(Projects, short_name = project)
	#return render(request, 'main/' + project.template, {'project': project})
	return render(request, 'main/project.html')

def projectList(request):
	#projectList = get_list_or_404(Projects)
	#return render(request, 'main/projects.html', {'projectList': projectList})
	return render(request, 'main/projects.html')

def news(request, project):
	#project = get_object_or_404(Projects, short_name = project)
	#return render(request, 'main/' + project.template, {'project': project})
	return render(request, 'main/news.html')

def newsList(request):
	#projectList = get_list_or_404(Projects)
	#return render(request, 'main/newsList.html', {'projectList': projectList})
	return render(request, 'main/newsList.html')