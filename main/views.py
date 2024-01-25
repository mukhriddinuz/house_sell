from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

def index_view(request):
    context = {
        'site_info': SiteInfo.objects.last(),
        'banner': Banner.objects.last(),
        'house': House.objects.all().order_by("-id")[:5],
        'testimonials': Testimonials.objects.all().order_by("-id")[:5],
        'about_homes': AboutHomes.objects.all().order_by("'id")[:4],
        'contact': Contact.objects.last()
    }
    return render(request, "index.html", context)



