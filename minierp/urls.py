from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponseRedirect


urlpatterns = [
    url(r'^$', lambda x: HttpResponseRedirect('/admin')),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/', "django.contrib.auth.views.logout", {'next_page': '/'}, name="logout"),
    url(r'^report_builder/', include('report_builder.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                             document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
