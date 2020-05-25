from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'intents', views.IntentViewSet)
router.register(r'keywords', views.KeywordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
