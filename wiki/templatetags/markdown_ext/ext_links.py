__all__ = ['ExtLinkExtension']

import re
import xml.etree.ElementTree as etree

from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
import requests


def build_url(label, base, end):
    """ Build a url from the label, a base, and an end. """
    clean_label = re.sub(r'([ ]+_)|(_[ ]+)|([ ]+)', '_', label)
    return '{}{}{}'.format(base, clean_label, end)


class ExtLinkExtension(Extension):

    def __init__(self, **kwargs):
        self.config = {
            'base_url': ['/', 'String to append to beginning or URL.'],
            'end_url': ['/', 'String to append to end of URL.'],
            'html_class': ['extlink', 'CSS hook. Leave blank for none.'],
            'build_url': [build_url, 'Callable formats URL from label.'],
        }

        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        self.md = md

        # append to end of inline patterns
        EXTLINK_RE = r'\[\[Ext:([\w0-9_ -]+)\]\]'
        extlinkPattern = ExtLinksInlineProcessor(EXTLINK_RE, self.getConfigs())
        extlinkPattern.md = md
        md.inlinePatterns.register(extlinkPattern, 'extlink', 75)


class ExtLinksInlineProcessor(InlineProcessor):
    def __init__(self, pattern, config):
        super().__init__(pattern)
        self.config = config

    def handleMatch(self, m, data):
        if m.group(1).strip():
            base_url, end_url, html_class = self._getMeta()
            label = m.group(1).strip()
            call_url = self.config['build_url'](label, base_url, end_url)
            try:
                info = requests.get(call_url).json()['data']
                a = etree.Element('a')
                a.text = label + ' [external]'
                a.set('href', info['url'])
                if html_class:
                    a.set('class', html_class)
            except (requests.exceptions.HTTPError, KeyError):
                a = ''
        else:
            a = ''
        return a, m.start(0), m.end(0)

    def _getMeta(self):
        """ Return meta data or config data. """
        base_url = self.config['base_url']
        end_url = self.config['end_url']
        html_class = self.config['html_class']
        if hasattr(self.md, 'Meta'):
            if 'ext_base_url' in self.md.Meta:
                base_url = self.md.Meta['ext_base_url'][0]
            if 'ext_end_url' in self.md.Meta:
                end_url = self.md.Meta['ext_end_url'][0]
            if 'ext_html_class' in self.md.Meta:
                html_class = self.md.Meta['ext_html_class'][0]
        return base_url, end_url, html_class


def makeExtension(**kwargs):  # pragma: no cover
    return ExtLinkExtension(**kwargs)
