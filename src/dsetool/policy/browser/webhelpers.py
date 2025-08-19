from euphorie.client.browser.webhelpers import WebHelpers
from plone.memoize.instance import memoize


class DSEToolWebHelpers(WebHelpers):
    """Browser view with utility methods that can be used in templates.
    View name: @@webhelpers
    """

    @property
    @memoize
    def custom_js(self):
        """Return custom JavaScript where necessary."""
        glossary_js = (
            f'<script src="{self.client_url}/++resource++dsetool.resources/'
            f'javascript/glossary.js" type="text/javascript"></script>'
        )
        return glossary_js

    @property
    @memoize
    def custom_css(self):
        """Return custom CSS where necessary."""
        styles_css = (
            f'<link href="{self.client_url}/++resource++dsetool.resources/'
            f'style/all.css" rel="stylesheet" type="text/css" />'
        )
        return styles_css
