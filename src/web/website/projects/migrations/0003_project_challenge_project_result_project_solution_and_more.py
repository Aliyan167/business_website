# Generated by Django 4.2 on 2024-09-28 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_client_projectstatus_projectclient_project_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='challenge',
            field=models.TextField(default='default_value', max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='result',
            field=models.TextField(default='default_value', max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='solution',
            field=models.TextField(default='default_value', max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(default='default_value', max_length=255),
        ),
    ]
