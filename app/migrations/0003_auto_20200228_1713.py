# Generated by Django 3.0.2 on 2020-02-28 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200228_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thingtodo',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='creation_date',
        ),
    ]
