# Generated by Django 3.1.2 on 2020-10-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_cv_generator_app', '0021_auto_20201017_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='web_cv_photo.jpg', null=True, upload_to='images/'),
        ),
    ]
