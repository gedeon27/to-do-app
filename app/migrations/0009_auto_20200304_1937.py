# Generated by Django 3.0.3 on 2020-03-04 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_userlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlist',
            name='things',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ThingToDo'),
        ),
    ]