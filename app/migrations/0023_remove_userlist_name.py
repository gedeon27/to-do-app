# Generated by Django 3.0.3 on 2020-03-24 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20200324_0907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlist',
            name='name',
        ),
    ]