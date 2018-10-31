from django.conf.urls import include, url
from rest_framework import routers
from drf_api.monitoring import urls as monitoring

router = routers.DefaultRouter()

urlpatterns = [
                  url(r'^', include(router.urls)),
              ] + monitoring.urlpatterns
