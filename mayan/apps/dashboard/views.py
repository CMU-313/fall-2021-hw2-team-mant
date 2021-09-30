from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

class DashboardListView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "test.html")
        #return HttpResponse('Hello, World!')
