# Generated by Django 5.0.6 on 2024-07-22 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_rename_img_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='base_static/global/media/'),
        ),
    ]
