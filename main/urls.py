from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^articles/&', views.articles, name='articles'),
    url(r'^article/(?P<article>\w+)/$', views.article, name='article'),
    url(r'^projects/', views.projects, name='projects'),
	url(r'^project/(?P<project>\w+)/$', views.project, name='project'),
    url(r'^department/(?P<department>\w+)/$', views.department, name='department'),
)