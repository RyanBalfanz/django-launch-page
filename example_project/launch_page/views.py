import json

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView

from .forms import InquiryForm
from .models import Inquiry


def home(request):
	return HttpResponse("It worked.")


class AjaxableResponseMixin(object):
	"""
	Mixin to add AJAX support to a form.
	Must be used with an object-based FormView (e.g. CreateView)
	"""
	def render_to_json_response(self, context, **response_kwargs):
		data = json.dumps(context)
		response_kwargs['content_type'] = 'application/json'
		return HttpResponse(data, **response_kwargs)

	def form_invalid(self, form):
		if self.request.is_ajax():
			return self.render_to_json_response(form.errors, status=400)
		else:
			return super(AjaxableResponseMixin, self).form_invalid(form)

	def form_valid(self, form):
		if self.request.is_ajax():
			data = {
				'first_name': form.instance.first_name,
				'last_name': form.instance.last_name,
				'email_address': form.instance.email_address,
			}

			Inquiry.objects.create(
				first_name=form.instance.first_name,
				last_name=form.instance.last_name,
				email_address=form.instance.email_address,
				ip_address=self.request.META['REMOTE_ADDR'],
			)

			return self.render_to_json_response(data)
		else:
			return super(AjaxableResponseMixin, self).form_valid(form)


class InquiryCreate(AjaxableResponseMixin, CreateView):
	model = Inquiry
	form_class = InquiryForm
	# template_name = "launch_page/inquiry_form.html"
	success_url = reverse_lazy('launch_page_inquire_thanks')


class InquiryCreateSuccess(TemplateView):
	template_name = "launch_page/thanks.html"


create_inquiry = InquiryCreate.as_view()
create_inquiry_success = InquiryCreateSuccess.as_view()
