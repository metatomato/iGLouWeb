from django.conf.urls import patterns,url

urlpatterns = patterns('',
    url(r'^$', 'studio.views.view_home', name='home'),
    url(r'^(?P<request_inner>\w*)/$', 'studio.views.view_inners'),
)
