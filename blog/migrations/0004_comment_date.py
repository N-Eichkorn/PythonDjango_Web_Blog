# Generated by Django 4.0.4 on 2022-05-10 20:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 10, 20, 54, 42, 70629, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
