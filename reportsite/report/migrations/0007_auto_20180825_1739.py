# Generated by Django 2.1 on 2018-08-25 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0006_auto_20180825_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
