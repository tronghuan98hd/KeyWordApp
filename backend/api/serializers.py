from rest_framework import serializers
from .models import Intent, Keyword, SampleKeyword


class SampleKeywordSerializers(serializers.ModelSerializer):
    class Meta:
        model = SampleKeyword
        fields = ('_id', 'keywords',)


class IntentSerializers(serializers.ModelSerializer):
    keywords = SampleKeywordSerializers(many=True)

    class Meta:
        model = Intent
        fields = ('_id', 'receipt', 'status', 'keywords')


class KeywordSerializers(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ('keyword',)
