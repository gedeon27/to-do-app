# Generated by Django 3.0.2 on 2020-03-09 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20200305_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='its_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list', related_query_name='userlist', to='app.UserList'),
        ),
    ]
