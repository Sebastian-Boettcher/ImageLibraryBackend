# Generated by Django 4.0.4 on 2022-05-18 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_rename_image_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='description',
        ),
    ]