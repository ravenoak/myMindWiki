__all__ = ['PageListView', 'PageDetailView', 'PageSearchView',
           'PageCreateView', 'PageUpdateView', 'TagListView', 'TagDetailView',
           'WebLinkDetailView', 'WebLinkSearchView', 'WebLinkListView',
           'TagSearchView']

from .page import (
    PageListView, PageDetailView, PageSearchView, PageCreateView,
    PageUpdateView,
)
from .tag import (
    TagListView, TagDetailView, TagSearchView,
)
from .weblink import (
    WebLinkDetailView, WebLinkSearchView, WebLinkListView,
)
