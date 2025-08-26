from osha.oira.content.browser.choice import EditForm as ChoiceEditForm
from osha.oira.content.browser.option import EditForm as OptionEditForm
from osha.oira.content.browser.recommendation import EditForm as RecommendationEditForm
from osha.oira.ploneintranet.quaive_mixin import QuaiveEditFormMixin


class ChoiceQuaiveEditForm(QuaiveEditFormMixin, ChoiceEditForm):
    """Custom edit form designed to be embedded in Quaive"""


class OptionQuaiveEditForm(QuaiveEditFormMixin, OptionEditForm):
    """Custom edit form designed to be embedded in Quaive"""


class RecommendationQuaiveEditForm(QuaiveEditFormMixin, RecommendationEditForm):
    """Custom edit form designed to be embedded in Quaive"""
