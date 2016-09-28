from django.conf.urls import include, url
from rest_framework import routers

from portfolio import views

router = routers.SimpleRouter()
router.register(r'tag', views.TagViewSet, 'tags')
router.register(r'developer', views.DeveloperViewSet, 'developers')
router.register(r'entry', views.EntryViewSet, 'entries')

urlpatterns = [
    url(r'^', include(router.urls)),
]
