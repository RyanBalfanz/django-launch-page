from django.db import models


INQUIRY_FIRST_NAME_MAX_LENGTH = 255
INQUIRY_LAST_NAME_MAX_LENGTH = 255


class Inquiry(models.Model):
	first_name = models.CharField(blank=True, null=True, max_length=INQUIRY_FIRST_NAME_MAX_LENGTH)
	last_name = models.CharField(blank=True, null=True, max_length=INQUIRY_LAST_NAME_MAX_LENGTH)
	email_address = models.EmailField()
	ip_address = models.GenericIPAddressField(blank=True, null=True, editable=False)
	creation_time = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Inquiry"
		verbose_name_plural = "Inquiries"

	def __unicode__(self):
		return self.email_address
