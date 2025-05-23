# Generated by Django 4.2 on 2025-03-14 18:53

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branding', '0004_personalbranding_apple_touch_icon_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalbranding',
            name='css_variables',
        ),
        migrations.RemoveField(
            model_name='personalbranding',
            name='extract_colors',
        ),
        migrations.AddField(
            model_name='personalbranding',
            name='Primary_color',
            field=colorfield.fields.ColorField(default='none', image_field=None, max_length=25, samples=None),
        ),
        migrations.AddField(
            model_name='personalbranding',
            name='background_color',
            field=colorfield.fields.ColorField(default='none', image_field=None, max_length=25, samples=None),
        ),
        migrations.AddField(
            model_name='personalbranding',
            name='button_color',
            field=colorfield.fields.ColorField(default='none', image_field=None, max_length=25, samples=None),
        ),
        migrations.AddField(
            model_name='personalbranding',
            name='button_text_color',
            field=colorfield.fields.ColorField(default='none', image_field=None, max_length=25, samples=None),
        ),
        migrations.AddField(
            model_name='personalbranding',
            name='dark_Primary_color',
            field=colorfield.fields.ColorField(default='none', image_field=None, max_length=25, samples=None),
        ),
        migrations.AddField(
            model_name='personalbranding',
            name='dark_background_color',
            field=colorfield.fields.ColorField(default='none', image_field=None, max_length=25, samples=None),
        ),
        migrations.AddField(
            model_name='personalbranding',
            name='dark_button_color',
            field=colorfield.fields.ColorField(default='none', image_field=None, max_length=25, samples=None),
        ),
        migrations.AddField(
            model_name='personalbranding',
            name='dark_button_text_color',
            field=colorfield.fields.ColorField(default='none', image_field=None, max_length=25, samples=None),
        ),
        migrations.AddField(
            model_name='personalbranding',
            name='dark_hover_color',
            field=colorfield.fields.ColorField(default='none', image_field=None, max_length=25, samples=None),
        ),
        migrations.AddField(
            model_name='personalbranding',
            name='dark_secondary_color',
            field=colorfield.fields.ColorField(default='none', image_field=None, max_length=25, samples=None),
        ),
        migrations.AddField(
            model_name='personalbranding',
            name='dark_text_color',
            field=colorfield.fields.ColorField(default='none', image_field=None, max_length=25, samples=None),
        ),
        migrations.AddField(
            model_name='personalbranding',
            name='hover_color',
            field=colorfield.fields.ColorField(default='none', image_field=None, max_length=25, samples=None),
        ),
        migrations.AddField(
            model_name='personalbranding',
            name='secondary_color',
            field=colorfield.fields.ColorField(default='none', image_field=None, max_length=25, samples=None),
        ),
        migrations.AddField(
            model_name='personalbranding',
            name='text_color',
            field=colorfield.fields.ColorField(default='none', image_field=None, max_length=25, samples=None),
        ),
    ]
