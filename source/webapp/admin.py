from django.contrib import admin
from webapp.models import Task


@admin.register(Task)
class ModelNameAdmin(admin.ModelAdmin):
    pass

