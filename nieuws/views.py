# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from nieuws.models import Artikel 

def index(request):
    artikelen = Artikel.objects.all().order_by('-datum')[:5]
    return render_to_response('nieuws/nieuws.html', {"artikelen": artikelen});

def list(request):
    artikelen = Artikel.objects.all().order_by('-datum')
    return render_to_response('nieuws/nieuws.html', {"artikelen": artikelen});

def detail(request, artikel_id):
    artikel = get_object_or_404(Artikel, pk=artikel_id)
    return render_to_response('nieuws/detail.html', {'artikel': artikel})
