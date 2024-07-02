# Generated by Django 5.0.1 on 2024-06-30 13:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='youtube_url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]