# Generated by Django 5.1.7 on 2025-05-23 19:25

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branding', '0015_alter_personalbranding_dark_mode_profile_picture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalbranding',
            name='og_image',
            field=models.ImageField(blank=True, help_text='Upload your Open Graph image. This will be used when sharing your website on social media.', null=True, storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='branding/og_image/'),
        ),
        migrations.AddField(
            model_name='personalbranding',
            name='this_site_url',
            field=models.URLField(blank=True, help_text='Enter the URL of your website. This will be used for Open Graph and Twitter Card meta tags.', null=True),
        ),
    ]
