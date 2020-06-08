from . import views
from rest_framework import routers
from django.urls import path, include
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'intents', views.IntentViewSet)
router.register(r'keywords', views.KeywordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'update_data/$', views.update_data, name='update_data'),
]
