# Generated by Django 3.0.2 on 2020-02-28 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200228_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='thing',
            new_name='task',
        ),
    ]
