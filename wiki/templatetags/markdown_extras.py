from django import template
from django.template.defaultfilters import stringfilter

import markdown as md
from plantuml_markdown import PlantUMLMarkdownExtension

register = template.Library()


@register.filter()
@stringfilter
def markdown(text):
    return md.markdown(text, extensions=['codehilite',
                                         'fenced_code',
                                         'tables',
                                         'toc',
                                         'wikilinks',
                                         PlantUMLMarkdownExtension()])
