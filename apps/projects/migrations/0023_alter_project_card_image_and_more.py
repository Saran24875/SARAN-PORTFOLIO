# Generated by Django 5.1.7 on 2025-05-23 19:25

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_alter_project_card_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Card_image',
            field=models.ImageField(help_text='this image will be displayed on the project card', null=True, storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='projects/images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='Project_image_1',
            field=models.ImageField(null=True, storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='projects/images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='Project_image_2',
            field=models.ImageField(null=True, storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='projects/images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='Project_image_3',
            field=models.ImageField(null=True, storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='projects/images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='Project_image_4',
            field=models.ImageField(null=True, storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='projects/images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='Project_image_5',
            field=models.ImageField(null=True, storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='projects/images/'),
        ),
    ]
