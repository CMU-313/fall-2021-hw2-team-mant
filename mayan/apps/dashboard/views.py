from django.http import HttpResponse
from django.views import View

class DashboardListView(View):

    def get(self, request, *args, **kwargs):
        html = "<html><body>THIS IS MY HTML CODE</body></html>"
        return HttpResponse(html)
