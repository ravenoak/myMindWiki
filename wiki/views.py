from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Page


class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    context_object_name = 'latest_page_list'
    def get_queryset(self):
        """Return the last five published pages."""
        return Page.objects.order_by('-date_created')  #[:5]

class DetailView(generic.DetailView):
    model = Page
    template_name = 'pages/detail.html'
