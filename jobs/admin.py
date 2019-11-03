from django.contrib import admin

from .models import Job, Details, Tag

admin.site.register(Tag)
admin.site.register(Details)
admin.site.register(Job)
