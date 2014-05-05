from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),

	#Articles
	url(r'^article/all/$', views.articleList, name='articleList'),
    url(r'^article/(?P<article>\w+)/$', views.article, name='article'),

    #Projects
    url(r'^project/all/$', views.projectList, name='projectList'),
	url(r'^project/(?P<project>\w+)/$', views.project, name='project'),

	#Departments
    url(r'^department/(?P<department>\w+)/$', views.department, name='department'),

    #News
    url(r'^news/all/$', views.newsList, name='newsList'),
	url(r'^news/(?P<news_id>\w+)/$', views.news, name='news'),
)