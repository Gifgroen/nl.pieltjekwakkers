# Create your views here.
from django.shortcuts import render_to_response
from gastenboek.models import Reactie

def list(request):
    r = Reactie.objects.all()
    return render_to_response('gastenboek/list.html', {'reacties': r}) # TODO