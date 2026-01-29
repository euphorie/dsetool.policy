from euphorie.client import utils
from plone import api
from zope.publisher.browser import BrowserView


class ListQuestions(BrowserView):
    """List all the questions for this survey"""

    def set_language(self):
        utils.setLanguage(
            self.request, self.context, getattr(self.context, "language", None)
        )

    def question_titles(self):
        self.set_language()
        brains = api.content.find(
            context=self.context,
            object_provides="euphorie.content.module.IModule",
            sort_on="getObjPositionInParent",
        )
        question_list = []
        for module in modules:
            module_path = module.getPath()
            questions = pc.searchResults(
                object_provides="euphorie.content.choice.IChoice",
                path={"query": module_path},
                sort_on="getObjPositionInParent",
            )
            for question in questions:
                question_list.append(question.Title)
        return question_list
