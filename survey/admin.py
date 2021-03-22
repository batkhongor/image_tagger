from django.contrib import admin

# Register your models here.
from survey import models

admin.site.register(models.Survey)