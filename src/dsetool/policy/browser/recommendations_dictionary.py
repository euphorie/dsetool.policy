from base64 import b64encode
from collections import defaultdict
from euphorie.client import MessageFactory as _
from euphorie.client import utils
from euphorie.client.browser.pdf import PdfView
from euphorie.client.browser.report import ReportInventory
from pkg_resources import resource_filename
from plone import api
from plone.memoize.view import memoize
from urllib.parse import quote


class RecommendationsDictionary(ReportInventory):
    """Instead of generating the Report Inventory which shows the results of a
    particular session, we display all the recommendations for all modules.
    """

    def get_all_options(self, module):
        for choice in module.values():
            for option in choice.values():
                yield option

    @property
    @memoize
    def country_code(self):
        return self.context.aq_parent.aq_parent.id

    @property
    @memoize
    def cover(self):
        filename = resource_filename(
            "euphorie.client.browser", f"templates/dsetool_dictionary_cover_{self.country_code}.png"
        )
        with open(filename, "rb") as data:
            return b64encode(data.read())

    @property
    @memoize
    def logo(self):
        filename = resource_filename(
            "euphorie.client.browser", f"templates/dsetool_dictionary_logo_{self.country_code}.png"
        )
        with open(filename, "rb") as data:
            return b64encode(data.read())

    @memoize
    def modules(self):
        return [
            module
            for module in self.context.values()
            if module.title != "label_custom_risks"
        ]


class RecommendationsDictionaryPDF(PdfView):
    """Re-use the parts from the @@pdf view to generate a PDF file from a view."""

    def __call__(self):
        context = self.context
        view = api.content.get_view("recommendations-dictionary", context, self.request)
        pdf = self.view_to_pdf(view)
        filename = f"Recommentations Dictionary - {context.title}.pdf"

        context.REQUEST.RESPONSE.setHeader("Content-Type", "application/pdf")
        context.REQUEST.RESPONSE.setHeader(
            "Content-Disposition", "attachment;filename*=UTF-8''%s" % quote(filename)
        )
        return pdf
