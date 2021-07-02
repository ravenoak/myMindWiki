from django.contrib import admin

from .models import Page, PageAdmin, Tag, TagAdmin, WebLink, WebLinkAdmin

admin.site.register(Page, PageAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(WebLink, WebLinkAdmin)
