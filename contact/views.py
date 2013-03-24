# Create your views here.
from django.shortcuts import render_to_response

def info(request):
    return render_to_response('contact/info.html', {})