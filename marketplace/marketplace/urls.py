from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
import client.urls


urlpatterns = [
    # Examples:
    # url(r'^$', 'marketplace.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^client/', include(client.urls)),
]
