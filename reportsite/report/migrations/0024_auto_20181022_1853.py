# Generated by Django 2.1 on 2018-10-22 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0023_auto_20181012_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officenetworkspeed',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='reportfield',
            name='report_type',
        ),
        migrations.RemoveField(
            model_name='reportlog',
            name='author',
        ),
        migrations.RemoveField(
            model_name='reportlog',
            name='type',
        ),
        migrations.RemoveField(
            model_name='reportlogvalue',
            name='field',
        ),
        migrations.RemoveField(
            model_name='reportlogvalue',
            name='report_log',
        ),
        migrations.DeleteModel(
            name='OfficeNetworkSpeed',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='ReportField',
        ),
        migrations.DeleteModel(
            name='ReportLog',
        ),
        migrations.DeleteModel(
            name='ReportLogValue',
        ),
        migrations.DeleteModel(
            name='ReportType',
        ),
    ]
