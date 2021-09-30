from django.http import HttpResponse
from django.views import View

class DashboardListView(View):

    def get(self, request, *args, **kwargs):
        dashboard_html = open("dashboard_view.html", 'r')
        html = dashboard_html.read() 
        # html = "<html><body>THIS IS MY HTML CODE testing testing testing</body></html>"
        return HttpResponse(html)
