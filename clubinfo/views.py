# Create your views here
from django.shortcuts import render_to_response

def clubinfo(request):
	return render_to_response('clubinfo/info.html', {})