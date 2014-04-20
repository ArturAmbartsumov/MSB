from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^article/(?P<article>\w+)/', views.article, name='article'),
	#url(r'^(?P<department>\w+)/(?P<project>\w+)/', views.project, name='project'),
    #url(r'^(?P<department>\w+)/', views.department, name='department'),
)

    # ex: /polls/
    #url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    #url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),