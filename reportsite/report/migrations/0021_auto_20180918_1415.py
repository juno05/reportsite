# Generated by Django 2.1 on 2018-09-18 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0020_auto_20180918_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='document',
            field=models.ImageField(blank=True, null=True, upload_to='documents/%Y/%m/%d/'),
        ),
    ]
