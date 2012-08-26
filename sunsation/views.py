# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from nieuws.models import Artikel 

def index(request):
    artikelen = Artikel.objects.all().order_by('-datum')[:5]
    return render_to_response('sunsation/sunsation.html', {"artikelen": artikelen});