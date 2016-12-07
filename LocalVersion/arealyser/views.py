from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
import datetime 
from .models import *

# Create your views here.
def property_view(request):
    hello_name = "Peter"
    ppr = get_template('ppr.html')
    units = PPR.objects.all()
    html = ppr.render(Context({'sample': hello_name,'properties': units }))
    return HttpResponse(html)