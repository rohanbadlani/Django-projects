from django.conf.urls import patterns, include, url, static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AIC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
    url(r'^admin/', include(admin.site.urls)),
    url(r'^companies/', include('companies.urls', namespace = "companies")),
) 
#+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
