# Generated by Django 3.1.2 on 2020-11-20 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_cv_generator_app', '0024_auto_20201017_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.TextField(max_length=200),
        ),
    ]
