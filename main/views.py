from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from main.models import *
import datetime

#http://djbook.ru/rel1.6/topics/db/queries.html

def index(request):
	newsList = News.objects.filter(isFavorite = True).order_by('-pub_date')[:5]
	departmentsList = Departments.objects.exclude(short_name = 'msb')
	projectsList = Projects.objects.filter(isFavorite = True)[:10]

	memorandum = get_object_or_404(Articles, short_name = 'memorandum')
	bannersList = Banners.objects.all()
	contacts = get_object_or_404(Contacts)
	context = {
		'newsList': newsList,
		'departmentsList': departmentsList,
		'projectsList': projectsList,
		'memorandum': memorandum,
		'bannersList': bannersList,
		'contacts': contacts
	}
	return render(request, 'main/base_index.html', context)

def article(request, article):
	article = get_object_or_404(Articles, short_name = article)
	bannersList = Banners.objects.all()
	contacts = get_object_or_404(Contacts)
	context = {
		'article': article,
		'bannersList': bannersList,
		'contacts': contacts
	}
	return render(request, 'main/' + article.template, context)

def articleList(request):
	articlesList = Articles.objects.filter(pub_date__lte = datetime.datetime.now()).order_by('pub_date')[:10]
	bannersList = Banners.objects.all()
	contacts = get_object_or_404(Contacts)
	context = {
		'articlesList': articlesList,
		'bannersList': bannersList,
		'contacts': contacts
	}
	return render(request, 'main/base_articlList.html', context)

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
	return render(request, 'main/' + cur_department.template, context)

def project(request, project):
	project = get_object_or_404(Projects, short_name = project)
	bannersList = Banners.objects.all()
	contacts = get_object_or_404(Contacts)
	context = {
		'project': project,
		'bannersList': bannersList,
		'contacts': contacts
	}
	return render(request, 'main/' + project.template, context)

def projectList(request):
	projectsList = Projects.objects.all()[:10]
	bannersList = Banners.objects.all()
	contacts = get_object_or_404(Contacts)
	context = {
		'projectsList': projectsList,
		'bannersList': bannersList,
		'contacts': contacts
	}
	return render(request, 'main/base_projectList.html', context)

def news(request, news_id):
	news = get_object_or_404(News, pk = news_id)
	bannersList = Banners.objects.all()
	contacts = get_object_or_404(Contacts)
	context = {
		'news': news,
		'bannersList': bannersList,
		'contacts': contacts
	}
	return render(request, 'main/' + news.template, context)

def newsList(request):
	newsList = News.objects.filter(pub_date__lte = datetime.datetime.now(), isFavorite = True).order_by('-pub_date')[:5]
	bannersList = Banners.objects.all()
	contacts = get_object_or_404(Contacts)
	context = {
		'newsList': newsList,
		'bannersList': bannersList,
		'contacts': contacts
	}
	return render(request, 'main/base_newsList.html', context)

















