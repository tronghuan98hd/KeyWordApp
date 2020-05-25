from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Intent, Keyword
from .serializers import KeywordSerializers, IntentSerializers
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
# Create your views here.


class IntentViewSet(ModelViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    serializer_class = IntentSerializers
    queryset = Intent.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = Intent.objects.filter(status__exact=None)[:20]
        return queryset


class KeywordViewSet(ModelViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    serializer_class = KeywordSerializers
    queryset = Keyword.objects.all()
