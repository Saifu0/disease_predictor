from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('endpoints',views.PredictorView)

urlpatterns = [
    path('api/',include(router.urls)),
    path('status/',views.DiseasePredictor),
    path('',views.SymptomInput,name="input_data")
]