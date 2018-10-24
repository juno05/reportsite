# Generated by Django 2.1 on 2018-08-21 03:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '0002_auto_20180819_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationLogReport',
            fields=[
                ('report_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='report.Report')),
                ('info', models.IntegerField()),
                ('warn', models.IntegerField()),
                ('error', models.IntegerField()),
                ('cs', models.IntegerField()),
            ],
            bases=('report.report',),
        ),
        migrations.CreateModel(
            name='AppReport',
            fields=[
                ('report_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='report.Report')),
                ('login', models.BooleanField()),
                ('recharge', models.BooleanField()),
                ('wallet', models.BooleanField()),
                ('earn', models.BooleanField()),
                ('gem', models.BooleanField()),
            ],
            bases=('report.report',),
        ),
        migrations.AddField(
            model_name='report',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]