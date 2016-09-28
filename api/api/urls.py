import django
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from api.views import swagger_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('portfolio.urls')),
    url(r'^static/(.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^', swagger_view),
]
