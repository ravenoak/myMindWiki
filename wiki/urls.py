from django.urls import path
from django.views.generic.base import RedirectView

from .views import page, tag, weblink

app_name = 'wiki'
urlpatterns = [
    # FIXME: Change absolute URL used here to a Django resolved URL
    path('', RedirectView.as_view(url='/wiki/page/'), name='index'),

    # FIXME: Change absolute URL used here to a Django resolved URL
    path('page/', RedirectView.as_view(url='/wiki/page/list'),
         name='page-index'),
    path('page/list', page.PageListView.as_view(), name='page-list'),
    # TODO: Enable once auth is figured out
    # path('page/new', views.PageCreateView.as_view(), name='page-new'),
    path('page/search', page.PageSearchView.as_view(), name='page-search'),
    path('page/<slug:slug>/', page.PageDetailView.as_view(),
         name='page-detail'),
    # TODO: Enable once auth is figured out
    # path('page/<slug:slug>/edit', views.PageUpdateView.as_view(),
    #     name='page-edit'),

    # FIXME: Change absolute URL used here to a Django resolved URL
    path('tag/', RedirectView.as_view(url='/wiki/tag/list'), name='tag-index'),
    path('tag/list', tag.TagListView.as_view(), name='tag-list'),
    path('tag/search', tag.TagSearchView.as_view(), name='tag-search'),
    path('tag/<slug:slug>/', tag.TagDetailView.as_view(), name='tag-detail'),

    # FIXME: Change absolute URL used here to a Django resolved URL
    path('weblink/', RedirectView.as_view(url='/wiki/weblink/list'),
         name='weblink-index'),
    path('weblink/list', weblink.WebLinkListView.as_view(),
         name='weblink-list'),
    path('weblink/search', weblink.WebLinkSearchView.as_view(),
         name='weblink-search'),
    path('weblink/<slug:slug>/', weblink.WebLinkDetailView.as_view(),
         name='weblink-detail'),
]
