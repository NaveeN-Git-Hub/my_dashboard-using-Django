# Generated by Django 3.1.2 on 2020-10-12 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_cv_generator_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='privious_work',
            new_name='experience',
        ),
    ]
