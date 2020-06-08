from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_200_OK
from .models import Intent, Keyword, SampleKeyword
from .serializers import KeywordSerializers, IntentSerializers, SampleKeywordSerializers
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view
from bson import ObjectId
from django.shortcuts import get_object_or_404
import json


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


@api_view(['POST', ])
def update_data(request):
    data = request.data
    intent = Intent.objects.get(_id=data.get("intentId"))
    intent.status = 1

    sample = SampleKeyword.objects.get(_id=data.get("id"))
    sample.newkeywords = data.get("newkeywords")

    intent.save()
    sample.save()

    result = {'id': str(sample._id),
              'keywords': sample.keywords,
              'newkeywords': sample.newkeywords,
              'intentId': intent._id,
              'intent': intent.receipt,
              'status': intent.status}

    return Response(data=result, status=HTTP_200_OK)
