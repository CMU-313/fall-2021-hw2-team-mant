from django.http import HttpResponse
from django.views import View

class DashboardListView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')