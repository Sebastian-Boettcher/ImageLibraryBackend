# Generated by Django 4.0.4 on 2022-05-14 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_image_uploadedfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
    ]