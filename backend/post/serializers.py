from rest_framework import serializers
from .models import Intent, KeyWord, NewKeyWord


class NewKeyWordSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewKeyWord
        fields = ('name',)


class KeyWordSerializers(serializers.ModelSerializer):
    class Meta:
        model = KeyWord
        fields = ('name',)


class IntentSerializers(serializers.ModelSerializer):
    # newkeywords = NewKeyWordSerializers(many=True)
    keywords = KeyWordSerializers(many=True, read_only=True)

    class Meta:
        model = Intent
        fields = ('intentId', 'intent', 'keywords',)
