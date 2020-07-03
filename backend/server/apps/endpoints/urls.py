from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import EndpointInfoViewSet, AlgoInfoViewset, AlgoRequestViewset

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints",EndpointInfoViewSet,basename="endpoints")
router.register(r"algoinfo",AlgoInfoViewset,basename="algoinfo")
router.register(r"algorequest",AlgoRequestViewset,basename="algorequest")

urlpatterns = [
    url(r"^api/v1/",include(router.urls))
]