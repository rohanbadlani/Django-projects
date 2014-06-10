from django.conf.urls import url, patterns
	
from polls import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'^(?P<poll_id>\d+)/details/$', views.detail, name = 'poll_detail'),
	url(r'^(?P<poll_id>\d+)/results/$', views.results, name = 'poll_results'),
	url(r'^(?P<poll_id>\d+)/vote/$', views.votes, name = 'poll_votes'),
	
)

