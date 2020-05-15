from django.db import models

# Create your models here.


class Intent(models.Model):
    intentId = models.CharField(max_length=100, unique=True)
    intent = models.TextField(max_length=100, default="no content")
    # status = models.BooleanField(default=False)


class KeyWord(models.Model):
    name = models.TextField(max_length=100)
    intent = models.ForeignKey(
        Intent, to_field='intentId', on_delete=models.CASCADE)


class NewKeyWord(models.Model):
    name = models.TextField(max_length=100)
    intent = models.ForeignKey(
        Intent, to_field='intentId', on_delete=models.CASCADE)
