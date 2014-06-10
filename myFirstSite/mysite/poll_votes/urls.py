from django.conf.urls import patterns, url
from poll_votes import views
	
urlpatterns = patterns('', 
	url(r'^$', views.IndexView.as_view(), name = "index"), 
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name = "details"),
	url(r'^(?P<pk>\d+)/results/$', views.ResultView.as_view(), name = "results"),
	url(r'^(?P<poll_id>\d+)/votes/$', views.votes, name = "votes"),
)
	
