from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MSB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^', include('main.urls', namespace='main')),
)

if settings.DEBUG:
    if settings.MEDIA_ROOT:

        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    if settings.STATIC_ROOT:

    	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += staticfiles_urlpatterns()
