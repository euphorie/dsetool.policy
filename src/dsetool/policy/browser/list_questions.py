from euphorie.client import utils
from plone import api
from zope.publisher.browser import BrowserView


class ListQuestions(BrowserView):
    """List all the questions for this survey"""

    def __call__(self):
        utils.setLanguage(
            self.request, self.context, getattr(self.context, "language", None)
        )
        return self.index()

    def question_titles(self):
        brains = api.content.find(
            context = self.context,
            portal_type = ["euphorie.module", "euphorie.choice"],
            sort_on="getObjPositionInParent",
        )
        module_brains = [i for i in brains if i.portal_type == "euphorie.module"]
        choice_brains = [i for i in brains if i.portal_type == "euphorie.choice"]
        question_list = []
        for module_brain in module_brains:
            module_choices = []
            for choice_brain in choice_brains:
                if module_brain.getPath() in choice_brain.getPath():
                    module_choices.append(choice_brain)
            question_list += module_choices
        return [i.Title for i in question_list]
