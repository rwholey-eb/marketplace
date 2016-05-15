from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'marketplace.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name='index.html')),
]
