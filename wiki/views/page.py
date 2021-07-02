__all__ = ['PageCreateView', 'PageDetailView', 'PageListView',
           'PageSearchView', 'PageUpdateView']

from django.views import generic

from wiki.forms import PageForm
from wiki.models import Page


class PageCreateView(generic.CreateView):
    model = Page
    form_class = PageForm
    template_name = 'wiki/page/edit.html'


class PageUpdateView(generic.UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'wiki/page/edit.html'


class PageListView(generic.ListView):
    model = Page
    ordering = '-date_created'
    paginate_by = 9
    template_name = 'wiki/page/list.html'


class PageDetailView(generic.DetailView):
    model = Page
    template_name = 'wiki/page/detail.html'


class PageSearchView(generic.ListView):
    context_object_name = 'search_results'
    paginate_by = 9
    template_name = 'wiki/page/search.html'

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
