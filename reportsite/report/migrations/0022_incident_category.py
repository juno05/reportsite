# Generated by Django 2.1 on 2018-10-12 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0021_auto_20180918_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='category',
            field=models.ForeignKey(blank=True, limit_choices_to={'group': 'category'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='report.Code'),
        ),
    ]
