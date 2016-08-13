from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # prevent the extra are-you-sure-you-want-to-logout step on logout
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    url(r'^larb/', include('larb.urls')),
	
	url(r'^test/', include('rest.urls')),
	
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
	 url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
