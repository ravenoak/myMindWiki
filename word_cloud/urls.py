from django.urls import path

from . import views

app_name = 'word_cloud'
urlpatterns = [
    path('create/', views.create_word_cloud, name='create'),
]
