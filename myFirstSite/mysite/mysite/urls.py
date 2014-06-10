from django.conf.urls import patterns, include, url

from django.contrib import admin
from polls import urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'mysite.views.home', name = 'home'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^polls/', include('polls.urls', namespace = "polls")),
	url(r'^poll_votes/', include('poll_votes.urls', namespace = "poll_votes")),
	
)
