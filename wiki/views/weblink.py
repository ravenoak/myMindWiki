__all__ = ['WebLinkDetailView', 'WebLinkListView', 'WebLinkSearchView']

from django.http import JsonResponse
from django.views import generic

from wiki.models import WebLink


class WebLinkDetailView(generic.DetailView):
    model = WebLink
    template_name = 'wiki/weblink/detail.html'

    def get(self, request, *args, **kwargs):
        json_requested = self.request.GET.get('json', False)
        if json_requested and json_requested.lower() == 'true':
            weblink = self.get_object()
            data = {
                'description': weblink.description,
                'url': weblink.url,
            }
            return JsonResponse({'data': data})
        return super().get(request, *args, **kwargs)


class WebLinkListView(generic.ListView):
    model = WebLink
    ordering = '-last_verified'
    paginate_by = 9
    template_name = 'wiki/weblink/list.html'


class WebLinkSearchView(generic.ListView):
    context_object_name = 'search_results'
    paginate_by = 9
    template_name = 'wiki/weblink/search.html'

    def get_queryset(self):
        contains = self.request.GET.get('contains', None)
        tags = self.request.GET.get('tags', None)

        query_set = WebLink.objects.all()
        if tags is not None and tags != '':
            for tag in tags.split(','):
                query_set = query_set.filter(tags__name__contains=tag)
        if contains is not None and contains != '':
            query_set = query_set.filter(
                slug__contains=contains) | query_set.filter(
                description__contains=contains)
        return query_set
