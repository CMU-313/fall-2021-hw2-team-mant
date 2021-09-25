from django.template import RequestContext
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from mayan.apps.views.generics import ( SingleObjectListView )

from .icons import icon_cabinet
from .links import (
    link_dashboard
)

class DashboardListView(SingleObjectListView):

    def get_extra_context(self):
        return {
            'hide_link': True,
            'hide_object': True,
            'title': _('Dashboard'),
            'no_results_icon': icon_cabinet,
            'no_results_main_link': link_dashboard.resolve(
                context=RequestContext(request=self.request)
            ),
            'no_results_text': _('...'),
            'no_results_title': _('No dashboard available'),
        }