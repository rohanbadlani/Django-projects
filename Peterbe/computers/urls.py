from django.conf.urls import url, patterns
from computers import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = "index"),
	url(r'^details/$', views.details, name = "details"),
)
