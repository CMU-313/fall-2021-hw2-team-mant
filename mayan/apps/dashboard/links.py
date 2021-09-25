import copy

from django.utils.translation import ugettext_lazy as _

from mayan.apps.navigation.classes import Link

from .icons import ( icon_cabinet_create )

def condition_cabinet_is_root(context):
    return context['resolved_object'].is_root_node()

# Dashboard links
link_dashboard = Link(
    icon=icon_cabinet_create,
    text=_('Dashboard'), view='dashboard:dashboard'
)