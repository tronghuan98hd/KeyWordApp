from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Intent, NewKeyWord, KeyWord
from .serializers import NewKeyWordSerializers, KeyWordSerializers, IntentSerializers
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
# Create your views here.


class NewKeyWordViewSet(ModelViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    serializer_class = NewKeyWordSerializers
    queryset = NewKeyWord.objects.all()


class IntentViewSet(ModelViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    serializer_class = IntentSerializers
    queryset = Intent.objects.all()
