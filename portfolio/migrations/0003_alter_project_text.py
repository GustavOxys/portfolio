# Generated by Django 5.0.6 on 2024-07-22 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_skill_name_alter_skill_slug_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='text',
            field=models.TextField(max_length=600),
        ),
    ]
