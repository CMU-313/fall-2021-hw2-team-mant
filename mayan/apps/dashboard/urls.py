from django.conf.urls import url
from .views import ( DashboardListView )

urlpatterns_dashboard = [
    url(
        regex=r'^dashboard/$', name='dashboard',
        view=DashboardListView.as_view()
        )
]

urlpatterns = []
urlpatterns.extend(urlpatterns_dashboard)