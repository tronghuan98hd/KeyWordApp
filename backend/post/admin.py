from django.contrib import admin
from .models import NewKeyWord, KeyWord, Intent
# Register your models here.

admin.site.register(NewKeyWord)
admin.site.register(KeyWord)
admin.site.register(Intent)
