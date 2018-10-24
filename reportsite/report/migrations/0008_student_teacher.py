# Generated by Django 2.1 on 2018-08-26 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0007_auto_20180825_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('home_group', models.CharField(max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('class_group', models.CharField(max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
