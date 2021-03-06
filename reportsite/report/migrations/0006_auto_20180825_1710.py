# Generated by Django 2.1 on 2018-08-25 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_auto_20180825_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officenetworkspeedreport',
            name='download',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='officenetworkspeedreport',
            name='ping',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='officenetworkspeedreport',
            name='upload',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]
