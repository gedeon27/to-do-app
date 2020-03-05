# Generated by Django 3.0.2 on 2020-03-05 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200305_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlist',
            name='tasks_stored',
        ),
        migrations.AddField(
            model_name='task',
            name='its_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.UserList'),
        ),
        migrations.AlterField(
            model_name='userlist',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
