from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     url(r'^navbar/', include('navbar.urls')),
     url(r'^news/', include('news.urls')),
     url(r'^globe/$', 'studio.views.view_globe', name='globe'),
     url(r'^', include('studio.urls'), name='home'),
   # url(r'^admin/', include(admin.site.urls)),
)
