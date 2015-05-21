# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Incidents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketincident',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Date de publication', default=datetime.datetime(2015, 5, 20, 16, 54, 55, 667164, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
