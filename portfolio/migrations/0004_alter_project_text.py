# Generated by Django 5.0.6 on 2024-07-22 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]
