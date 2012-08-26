from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pieltjekwakkers.views.home', name='home'),
    # url(r'^pieltjekwakkers/', include('pieltjekwakkers.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'nieuws.views.index'),
    url(r'^declub/', 'clubinfo.views.clubinfo'),
    url(r'^sunsation/', 'sunsation.views.index'),
    url(r'^gastenboek/', 'gastenboek.views.list'),
    url(r'^nieuws/$', 'nieuws.views.list'),
    url(r'^nieuws/(?P<artikel_id>\d+)/$', 'nieuws.views.detail'),    
    url(r'^admin/', include(admin.site.urls)),
)
