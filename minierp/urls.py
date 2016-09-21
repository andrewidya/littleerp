from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'minierp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/', "django.contrib.auth.views.logout", {'next_page': '/'}, name="logout"),
    url(r'^crm/', include('crm.urls', namespace='crm', app_name='crm')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
