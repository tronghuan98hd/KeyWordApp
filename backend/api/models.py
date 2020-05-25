from django.db import models
import uuid

unique_id = uuid.uuid4().hex


class Intent(models.Model):
    _id = models.CharField(max_length=100,
                           primary_key=True, default=unique_id)
    receipt = models.CharField(max_length=200)
    status = models.BooleanField(default=False, blank=False)

    class Meta:
        db_table = 'intents'


class SampleKeyword(models.Model):
    _id = models.CharField(max_length=100,
                           primary_key=True, default=unique_id)
    keywords = models.CharField(max_length=200)
    intentId = models.ForeignKey(
        Intent, to_field='_id', on_delete=models.CASCADE, db_column='intentId', related_name='keywords')

    class Meta:
        db_table = 'keyword_samples'


class Keyword(models.Model):
    _id = models.CharField(max_length=100,
                           primary_key=True, default=unique_id)
    keyword = models.CharField(max_length=200)

    class Meta:
        db_table = 'keyword'
