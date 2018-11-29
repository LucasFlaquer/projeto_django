from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Disciplina)
admin.site.register(models.Curso)
admin.site.register(models.Coordenador)
admin.site.register(models.Disc_Curso)