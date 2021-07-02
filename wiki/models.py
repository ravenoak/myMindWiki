__all__ = ['Page', 'PageAdmin', 'Tag', 'TagAdmin', 'WebLink', 'WebLinkAdmin']

from django.contrib import admin
from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    tags = models.ManyToManyField('Tag')

    def __repr__(self):
        return self.slug

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('wiki:page-detail', kwargs={'slug': self.slug})


class PageAdmin(admin.ModelAdmin):
    autocomplete_fields = ['tags']
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['body__contains',
                     'slug__contains',
                     'title__contains',
                     'tags__name__contains']


class Tag(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __repr__(self):
        return self.slug

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('wiki:tag-detail', kwargs={'slug': self.slug})


class TagAdmin(admin.ModelAdmin):
    search_fields = ['description__contains',
                     'name__contains',
                     'slug__contains']


class WebLink(models.Model):
    slug = models.SlugField(unique=True)
    url = models.URLField(unique=True)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag')
    last_verified = models.DateTimeField(blank=True, null=True)

    def __repr__(self):
        return self.slug

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('wiki:weblink-detail', kwargs={'slug': self.slug})


class WebLinkAdmin(admin.ModelAdmin):
    autocomplete_fields = ['tags']
    search_fields = ['description__contains',
                     'slug__contains',
                     'url__contains',
                     'tags__name__contains']
