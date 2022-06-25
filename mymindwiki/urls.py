"""mymindwiki URL Configuration

"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

admin.site.site_header = "MindWiki"
admin.site.site_title = "MindWiki"
admin.site.index_title = "MindWiki Administration"

urlpatterns = [
    path('', RedirectView.as_view(url='/wiki/')),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
    path('wiki/', include('mindwiki.urls')),
    path('wordcloud/', include('word_cloud.urls')),
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
