# Generated by Django 4.0.4 on 2022-05-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_remove_upload_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='description',
            field=models.CharField(default='', max_length=600),
        ),
    ]
