from django.contrib import admin
from . models import Todo

from typing import Tuple

# Register your models here.

class TodoAdminModel(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(Todo, TodoAdminModel)