from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from main.models import *
import datetime

#http://djbook.ru/rel1.6/topics/db/queries.html

def index(request):
	newsList = News.objects.filter(pub_date__lte = datetime.datetime.now(), isFavorite = True).order_by('-pub_date')[:5]
	departmentsList = Departments.objects.exclude(short_name = 'msb')
	projectsList = Projects.objects.filter(department__short_name = 'msb')[:5]
	bannersList = Banners.objects.all()
	contacts = get_object_or_404(Contacts)
	context = {
		'newsList': newsList,
		'departmentsList': departmentsList,
		'projectsList': projectsList,
		'bannersList': bannersList,
		'contacts': contacts
	}

	return render(request, 'main/base_index.html', context)
	#return render(request, 'main/gallerie.html')

def article(request, article):
	article = get_object_or_404(Articles, short_name = article)
	bannersList = Banners.objects.all()
	contacts = get_object_or_404(Contacts)
	context = {
		'article': article,
		'bannersList': bannersList,
		'contacts': contacts
	}
	if article == 'article':
		return render(request, 'main/base_article.html', context)
	return render(request, 'main/article.html', context)

def articleList(request):
	articlesList = Articles.objects.filter(pub_date__lte = datetime.datetime.now()).order_by('pub_date')[:10]
	bannersList = Banners.objects.all()
	contacts = get_object_or_404(Contacts)
	context = {
		'articlesList': articlesList,
		'bannersList': bannersList,
		'contacts': contacts
	}
	return render(request, 'main/base_articles.html', articlesList)

def department(request, department):
	cur_department = get_object_or_404(Departments, short_name = department)
	projectsList = cur_department.projects_set.all()[:5]
	articlesList = cur_department.article.filter(pub_date__lte = datetime.datetime.now(), isFavorite = True).order_by('-pub_date')[:5]
	bannersList = Banners.objects.all()
	contacts = get_object_or_404(Contacts)
	context = {
		'department': cur_department,
		'projectsList': projectsList,
		'articlesList': articlesList,
		'bannersList': bannersList,
		'contacts': contacts
	}
	print context
	if department == 'lstp':
		return render(request, 'main/lstp.html')
	if department == 'RA':
		return render(request, 'main/RA.html')
	if department == 'buamzem':
		return render(request, 'main/buamzem.html')
	return render(request, 'main/department.html', context)

def project(request, project):
	project = get_object_or_404(Projects, short_name = project)
	bannersList = Banners.objects.all()
	contacts = get_object_or_404(Contacts)
	context = {
		'project': project,
		'bannersList': bannersList,
		'contacts': contacts
	}
	if project == '':
		return render(request, 'main/base_project.html')
	return render(request, 'main/project.html', context)

def projectList(request):
	projectsList = Projects.objects.all()[:10]
	bannersList = Banners.objects.all()
	contacts = get_object_or_404(Contacts)
	context = {
		'projectsList': projectsList,
		'bannersList': bannersList,
		'contacts': contacts
	}
	return render(request, 'main/projects.html', context)

def news(request, news_id):
	news = get_object_or_404(News, pk = news_id)
	bannersList = Banners.objects.all()
	contacts = get_object_or_404(Contacts)
	context = {
		'news': news,
		'bannersList': bannersList,
		'contacts': contacts
	}
	if news_id == 1:
		return render(request, 'main/news1.html')
	if news_id == 2:
		return render(request, 'main/news2.html')
	return render(request, 'main/news.html', context)

def newsList(request):
	#projectList = get_list_or_404(Projects)
	newsList = News.objects.filter(pub_date__lte = datetime.datetime.now(), isFavorite = True).order_by('-pub_date')[:5]
	bannersList = Banners.objects.all()
	contacts = get_object_or_404(Contacts)
	context = {
		'newsList': newsList,
		'bannersList': bannersList,
		'contacts': contacts
	}
	return render(request, 'main/newsList.html', context)

















