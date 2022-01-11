from django.shortcuts import render
from django.views import View

from .models import Weather


class IndexView(View):

    def get(self, request, *args, **kwargs):

        context = {}
        context["weather"]  = Weather.objects.order_by("-dt").first()
        
        return render(request,"tenki/index.html",context)

index   = IndexView.as_view()
