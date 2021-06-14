import io

from django.http import HttpResponse
from django.views.decorators.http import require_GET
from wordcloud import WordCloud


@require_GET
def create_word_cloud(request):
    width = request.GET['width']
    height = request.GET['height']
    bg_color = tuple(int(request.GET['bg'][i:i + 2], 16) for i in (0, 2, 4))
    words = request.GET['words'].replace(' ', '')
    cmap = request.GET['cmap']

    wc = WordCloud(width=int(width),
                   height=int(height),
                   background_color=bg_color,
                   repeat=True,
                   colormap=cmap, )
    img = wc.generate(words)
    f = io.BytesIO()
    img.to_image().save(f, format='png')
    f.seek(0)
    return HttpResponse(f.read(), content_type='image/png')
