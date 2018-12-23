from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Usecase)
admin.site.register(models.Scenario)
admin.site.register(models.Step)
