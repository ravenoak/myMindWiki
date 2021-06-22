__all__ = ['Page', 'Tag', 'WebLink']

from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=32)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('wiki:page-detail', kwargs={'slug': self.slug})


class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class WebLink(models.Model):
    slug = models.SlugField(max_length=32)
    url = models.URLField()
    description = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag')
    last_verified = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('wiki:weblink-detail', kwargs={'slug': self.slug})
