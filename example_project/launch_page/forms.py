from django import forms

from .models import Inquiry


class InquiryForm(forms.ModelForm):
	class Meta:
		model = Inquiry
		fields = ('email_address', 'first_name', 'last_name')
