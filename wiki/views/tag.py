__all__ = ['TagDetailView', 'TagListView', 'TagSearchView']

from django.views import generic

from wiki.models import Tag


class TagDetailView(generic.DetailView):
    model = Tag
    template_name = 'wiki/tag/detail.html'


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 9
    template_name = 'wiki/tag/list.html'


class TagSearchView(generic.ListView):
    context_object_name = 'search_results'
    paginate_by = 9
    template_name = 'wiki/tag/search.html'

    def get_queryset(self):
        contains = self.request.GET.get('contains', None)

        query_set = Tag.objects.all()
        if contains is not None and contains != '':
            query_set = query_set.filter(
                name__contains=contains) | query_set.filter(
                slug__contains=contains) | query_set.filter(
                description__contains=contains)
        return query_set
