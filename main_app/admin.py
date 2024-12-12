from django.contrib import admin

from .models import Story, Tag

admin.site.register(Story)
admin.site.register(Tag)