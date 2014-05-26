from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from main.models import *
import datetime

#http://djbook.ru/rel1.6/topics/db/queries.html

def index(request):
	newsList = News.objects.filter(isFavorite = True).order_by('-pub_date')[:5]
	projectsList = Projects.objects.filter(isFavorite = True)[:10]
	memorandum = get_object_or_404(Articles, short_name__iexact = 'memorandum')
	context = {
		'isIndex': True,
		'newsList': newsList,
		'projectsList': projectsList,
		'memorandum': memorandum
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/base_index.html', context)

def article(request, article):
	article = get_object_or_404(Articles, short_name = article)
	context = {
		'isArticle': True,
		'article': article
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/' + article.template, context)

def articleList(request):
	articlesList = Articles.objects.all().order_by('pub_date')[:10]
	context = {
		'isArticleList': True,
		'articlesList': articlesList
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/base_articlList.html', context)

def department(request, department):
	cur_department = get_object_or_404(Departments, short_name = department)
	projectsList = cur_department.projects_set.all()[:5]
	articlesList = cur_department.article.filter(isFavorite = True).order_by('-pub_date')[:5]
	context = {
		'idDepartment': True,
		'department': cur_department,
		'projectsList': projectsList,
		'articlesList': articlesList
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/' + cur_department.template, context)

def project(request, project):
	project = get_object_or_404(Projects, short_name = project)
	context = {
		'isProject': True,
		'project': project
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/' + project.template, context)

def projectList(request):
	projectsList = Projects.objects.all()[:10]
	context = {
		'isProjectList': True,
		'projectsList': projectsList
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/base_projectList.html', context)

def news(request, news_id):
	news = get_object_or_404(News, pk = news_id)
	context = {
		'isNews': True,
		'news': news
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/' + news.template, context)

def newsList(request):
	newsList = News.objects.filter(isFavorite = True).order_by('-pub_date')[:5]
	context = {
		'isNewsList': True,
		'newsList': newsList
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/base_newsList.html', context)

def bmstu(request):
	bmstu = AboutBMSTU.objects.get()
	context = {
		'isNewsList': True,
		'newsList': newsList
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/base_bmstu.html', context)

def contacts(request):
	context = {
		'isContacts': True
	}
	context.update(getDefaultContext(request))
	return render(request, 'main/base_newsList.html', context)

def getDefaultContext(request):
	bannersList = Banners.objects.all()
	contacts = Contacts.objects.get()
	departmentsList = Departments.objects.exclude(short_name = 'msb')
	context = {
		'location': request.path,
		'departmentsList': departmentsList,
		'bannersList': bannersList,
		'contacts': contacts
	}
	return context

















