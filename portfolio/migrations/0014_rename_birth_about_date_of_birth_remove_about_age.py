# Generated by Django 5.0.6 on 2024-07-25 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_about_delete_sobre_alter_project_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='birth',
            new_name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='about',
            name='age',
        ),
    ]