from dsetool.policy.content.browser.choice import AddView as EuphorieChoiceAddView
from dsetool.policy.content.browser.option import AddView as EuphorieOptionAddView
from osha.oira.ploneintranet.quaive_create import QuaiveCreateFormMixin
from osha.oira.ploneintranet.quaive_create import QuaiveCreateViewMixin


from dsetool.policy.content.browser.recommendation import (  # isort:skip
    AddView as EuphorieRecommendationAddView,
)


class QuaiveCreateEuphorieChoiceForm(QuaiveCreateFormMixin, EuphorieChoiceAddView.form):
    pass
    # template = ViewPageTemplateFile("templates/quaive-form.pt")


class QuaiveCreateEuphorieChoiceView(QuaiveCreateViewMixin, EuphorieChoiceAddView):
    form = QuaiveCreateEuphorieChoiceForm


class QuaiveCreateEuphorieOptionForm(QuaiveCreateFormMixin, EuphorieOptionAddView.form):
    pass
    # template = ViewPageTemplateFile("templates/quaive-form.pt")


class QuaiveCreateEuphorieOptionView(QuaiveCreateViewMixin, EuphorieOptionAddView):
    form = QuaiveCreateEuphorieOptionForm


class QuaiveCreateEuphorieRecommendationForm(
    QuaiveCreateFormMixin, EuphorieRecommendationAddView.form
):
    pass


# template = ViewPageTemplateFile("templates/quaive-form.pt")


class QuaiveCreateEuphorieRecommendationView(
    QuaiveCreateViewMixin, EuphorieRecommendationAddView
):
    form = QuaiveCreateEuphorieRecommendationForm
