from django.conf.urls import url
from .views import ( DashboardListView )

urlpatterns = [
    url(
        regex=r'^dashboard/$', name='dashboard',
        view=DashboardListView.as_view()
        )
]