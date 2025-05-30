# Generated by Django 4.2 on 2025-01-27 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='social_media_links',
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='discord',
            field=models.CharField(blank=True, help_text='Discord username (e.g., username#1234)', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='reddit',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='threads',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='twitter',
            field=models.URLField(blank=True, help_text='Twitter/X profile link', null=True),
        ),
    ]
