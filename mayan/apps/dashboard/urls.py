from django.conf.urls import url
from .views import ( DashboardListView )

urlpatterns_dashboard = [
    url(
        regex=r'^dashboard/$', name='dashboard',
        view=DashboardListView.as_view(template_name = 'home.html')
        )
]

urlpatterns = []
urlpatterns.extend(urlpatterns_dashboard)