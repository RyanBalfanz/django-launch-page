from django.contrib import admin

from .models import Inquiry


class InquiryAdmin(admin.ModelAdmin):
	date_hierarchy = "creation_time"
	list_display = (
		"first_name",
		"last_name",
		"email_address",
		"ip_address",
		"creation_time",
	)


admin.site.register(Inquiry, InquiryAdmin)
