from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'intent', views.IntentViewSet)
router.register(r'newkeyword', views.NewKeyWordViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
