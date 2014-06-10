from django.conf.urls import url, patterns

from companies import views
	
urlpatterns = patterns('', 
	url(r'^$', views.index, name = "index"),
	url(r'^(?P<company_id>\d+)/', views.details, name = "details"),
	url(r'^discipline/$', views.discipline, name = "discipline"),
	url(r'^discipline/(?P<discipline_id>\d+)/$', views.specific, name = "specific"),
	
)
