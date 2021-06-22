from django import template
from django.template.defaultfilters import stringfilter

import markdown as md
from markdown.extensions.wikilinks import WikiLinkExtension
from plantuml_markdown import PlantUMLMarkdownExtension

from .markdown_ext.ext_links import ExtLinkExtension

register = template.Library()


@register.filter()
@stringfilter
def markdown(text):
    return md.markdown(
        text,
        extensions=['codehilite',
                    'fenced_code',
                    'tables',
                    'toc',
                    PlantUMLMarkdownExtension(),
                    WikiLinkExtension(base_url='/wiki/page/'),
                    ExtLinkExtension(
                        base_url='http://localhost:1312/wiki/weblink/', # FIXME
                        end_url='/?json=true')
                    ])
