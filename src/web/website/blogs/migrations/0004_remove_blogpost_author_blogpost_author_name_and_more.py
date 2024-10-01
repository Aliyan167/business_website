# Generated by Django 4.2 on 2024-09-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_author_rename_featured_image_blogpost_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='author',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='author_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]