from collections import defaultdict
from dsetool.policy import utils
from plone import api
from zope.i18n.locales import locales
from zope.publisher.browser import BrowserView


class ListQuestions(BrowserView):
    """List all the questions for this survey"""

    def question_titles(self) -> list[str]:
        """Return the titles of all questions in this survey.

        We fetch all modules and choices (modules children),
        then group the choices by their parent module path.

        Finally, we flatten the titles ordered by the modules.
        """
        brains = api.content.find(
            context=self.context,
            portal_type=["euphorie.module", "euphorie.choice"],
            sort_on="getObjPositionInParent",
        )

        modules_paths = []
        title_by_path = defaultdict(list)

        for brain in brains:
            if brain.portal_type == "euphorie.module":
                modules_paths.append(brain.getPath())
            elif brain.portal_type == "euphorie.choice":
                module_path = brain.getPath().rpartition("/")[0]
                title_by_path[module_path].append(brain.Title)

        titles = []
        for module_path in modules_paths:
            titles.extend(title_by_path[module_path])

        return titles

    def modified(self):
        return self.context.modified().asdatetime().date().isoformat()

    def __call__(self):
        utils.set_language(self.context, self.request)
        return super().__call__()
