from django.urls import path

from . import views

app_name = 'wiki'
urlpatterns = [
    path('', views.PageListView.as_view(), name='index'),
    path('search', views.PageSearchView.as_view(), name='search'),

    path('page/', views.PageListView.as_view(), name='page-list'),
    path('page/new', views.PageCreateView.as_view(), name='page-new'),
    path('page/<slug:slug>/', views.PageDetailView.as_view(),
         name='page-detail'),
    path('page/<slug:slug>/edit', views.PageUpdateView.as_view(),
         name='page-edit'),
]
