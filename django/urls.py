from django.conf.urls import include, url
from rest_framework import routers

from gwaithdemo import views

router = routers.DefaultRouter()
router.register(r'rates', views.RateViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
