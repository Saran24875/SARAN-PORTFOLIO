# Generated by Django 5.1.7 on 2025-05-16 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branding', '0011_personalbranding_profile_picture_for_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalbranding',
            name='about',
            field=models.TextField(blank=True, help_text='Enter your about. This will be displayed on the about Section.', null=True),
        ),
    ]
