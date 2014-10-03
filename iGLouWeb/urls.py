from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'studio.views.view_home', name='home'),
     url(r'^navbar/', include('navbar.urls')),

   # url(r'^admin/', include(admin.site.urls)),
)
