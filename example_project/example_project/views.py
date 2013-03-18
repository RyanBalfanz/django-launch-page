import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
	return HttpResponseRedirect(reverse('inquiry_create'))
