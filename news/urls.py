from django.conf.urls import patterns,url

urlpatterns = patterns('',
    url(r'^$', 'news.views.view_news', name='news'),
)
