__all__ = ['PageCreateView', 'PageDetailView', 'PageListView',
           'PageSearchView', 'PageUpdateView', 'WebLinkDetailView']

from django.http import JsonResponse
from django.views import generic, View

from .models import Page, WebLink
from .forms import PageForm


class PageCreateView(generic.CreateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/edit.html'


class PageUpdateView(generic.UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/edit.html'


class PageListView(generic.ListView):
    context_object_name = 'latest_page_list'
    model = Page
    ordering = '-date_created'
    paginate_by = 9
    template_name = 'pages/list.html'


class PageDetailView(generic.DetailView):
    model = Page
    template_name = 'pages/detail.html'


class PageSearchView(generic.ListView):
    context_object_name = 'search_results'
    paginate_by = 9
    template_name = 'pages/search.html'

    def get_queryset(self):
        contains = self.request.GET.get('contains', None)
        tags = self.request.GET.get('tags', None)

        query_set = Page.objects.all()
        if tags is not None and tags != '':
            for tag in tags.split(','):
                query_set = query_set.filter(tags__name__contains=tag)
        if contains is not None and contains != '':
            query_set = query_set.filter(
                body__contains=contains) | query_set.filter(
                title__contains=contains)
        return query_set


class WebLinkDetailView(generic.DetailView):
    model = WebLink

    def get(self, request, *args, **kwargs):
        json_requested = self.request.GET.get('json', False)
        if json_requested and json_requested.lower() =='true':
            weblink = self.get_object()
            data = {
                'description': weblink.description,
                'url': weblink.url,
            }
            return JsonResponse({'data': data})
        return super().get(request, *args, **kwargs)
