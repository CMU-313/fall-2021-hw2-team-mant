import copy

from django.utils.translation import ugettext_lazy as _

from mayan.apps.navigation.classes import Link

from .icons import ( icon_cabinet_create )


# Dashboard links
link_dashboard = Link(
    icon=icon_cabinet_create,
    text=_('Dashboard'), url="/dashboard/dashboard"
)