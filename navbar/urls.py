from django.conf.urls import patterns,url

urlpatterns = patterns('',
    url(r'^$', 'navbar.views.view_navbar', name='navbar'),
)
