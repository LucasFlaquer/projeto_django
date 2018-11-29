from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Professor)
admin.site.register(models.Professor_Disc)
admin.site.register(models.ProfDisc_Curso)
admin.site.register(models.PlanoDesc)
