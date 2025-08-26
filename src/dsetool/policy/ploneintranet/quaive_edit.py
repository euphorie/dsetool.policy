from dsetool.policy.content.browser.choice import EditForm as ChoiceEditForm
from dsetool.policy.content.browser.option import EditForm as OptionEditForm
from dsetool.policy.content.browser.recommendation import (
    EditForm as RecommendationEditForm,
)
from osha.oira.ploneintranet.quaive_mixin import QuaiveEditFormMixin


class ChoiceQuaiveEditForm(QuaiveEditFormMixin, ChoiceEditForm):
    """Custom edit form designed to be embedded in Quaive"""


class OptionQuaiveEditForm(QuaiveEditFormMixin, OptionEditForm):
    """Custom edit form designed to be embedded in Quaive"""


class RecommendationQuaiveEditForm(QuaiveEditFormMixin, RecommendationEditForm):
    """Custom edit form designed to be embedded in Quaive"""
