import json

from django.http import HttpResponse


def home(request):
	return HttpResponse("Cool stuff ahead")
