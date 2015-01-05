# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255, null=True, blank=True)),
                ('last_name', models.CharField(max_length=255, null=True, blank=True)),
                ('email_address', models.EmailField(max_length=75)),
                ('ip_address', models.GenericIPAddressField(editable=False, blank=True, null=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Inquiry',
                'verbose_name_plural': 'Inquiries',
            },
            bases=(models.Model,),
        ),
    ]
