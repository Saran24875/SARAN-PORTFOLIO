# Generated by Django 4.2 on 2025-02-07 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='icon',
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_type',
            field=models.CharField(choices=[('Programming Language', 'Programming Language'), ('Framework', 'Framework'), ('Tools', 'Tools'), ('Soft Skills', 'Soft Skills')], max_length=50, unique=True),
        ),
        migrations.DeleteModel(
            name='SkillType',
        ),
    ]
