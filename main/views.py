from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from main.models import *
import datetime

#http://djbook.ru/rel1.6/topics/db/queries.html

def index(request):
	#articleList = get_list_or_404(ArticleDescriptions)
	#return render(request, 'main/index.html', {'articleList': articleList})
	#lastNews = get_list_or_404(News, pub_date__lte=datetime.datetime.now(), isFavorite=True).order_by('pub_date')[:5]
	newsList = News.objects.filter(pub_date__lte = datetime.datetime.now(), isFavorite = True).order_by('-pub_date')[:5]
	departmentsList = Departments.objects.exclude(short_name = 'msb')
	projectsList = Projects.objects.filter(department__short_name = 'msb')[:5]
	context = {
		'newsList': newsList,
		'departmentsList': departmentsList,
		'projectsList': projectsList,
	}
	return render(request, 'main/index.html', context)

def article(request, article):
	#article = get_object_or_404(Articles, short_name = article)
	#return render(request, 'main/' + article.template, {'article': article})
	article = get_object_or_404(Articles, short_name = article)
	context = {
		'article': article
	}
	if article == 'article':
		return render(request, 'main/article.html', context)
	return render(request, 'main/article.html', context)

def articleList(request):
	#articleList = get_list_or_404(ArticleDescriptions)
	#return render(request, 'main/articles.html', {'articleList': articleList})
	articlesList = Articles.objects.filter(pub_date__lte = datetime.datetime.now()).order_by('-pub_date')[:10]
	context = {
		'articlesList': articlesList
	}
	return render(request, 'main/articles.html', articlesList)

def department(request, department):
	#department = get_object_or_404(Departments, short_name = department)
	#return render(request, 'main/' + department.template, {'department': department})
	cur_department = get_object_or_404(Departments, short_name = department)
	projectsList = cur_department.projects_set.all()[:5]
	articlesList = cur_department.article.filter(pub_date__lte = datetime.datetime.now(), isFavorite = True).order_by('-pub_date')[:5]
	context = {
		'department': cur_department,
		'projectsList': projectsList,
		'articlesList': articlesList
	}
	print context
	if department == 'lstp':
		return render(request, 'main/lstp.html')
	if department == 'RA':
		return render(request, 'main/RA.html')
	if department == 'buamzem':
		return render(request, 'main/buamzem.html')
	return render(request, 'main/department.html')

def project(request, project):
	#project = get_object_or_404(Projects, short_name = project)
	#return render(request, 'main/' + project.template, {'project': project})
	if project == '':
		return render(request, 'main/project.html')
	return render(request, 'main/project.html')

def projectList(request):
	#projectList = get_list_or_404(Projects)
	#return render(request, 'main/projects.html', {'projectList': projectList})
	return render(request, 'main/projects.html')

def news(request, news_id):
	#project = get_object_or_404(Projects, short_name = project)
	#return render(request, 'main/' + project.template, {'project': project})
	if news_id == 1:
		return render(request, 'main/news1.html')
	if news_id == 2:
		return render(request, 'main/news2.html')
	return render(request, 'main/news.html')

def newsList(request):
	#projectList = get_list_or_404(Projects)
	#return render(request, 'main/newsList.html', {'projectList': projectList})
	return render(request, 'main/newsList.html')