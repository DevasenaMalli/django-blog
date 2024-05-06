# Generated by Django 5.0.4 on 2024-05-04 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_blog_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='github_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='linkedin_link',
            field=models.URLField(blank=True),
        ),
    ]