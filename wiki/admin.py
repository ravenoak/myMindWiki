from django.contrib import admin

from .models import Page, Tag, WebLink

admin.site.register(Page)
admin.site.register(Tag)
admin.site.register(WebLink)
