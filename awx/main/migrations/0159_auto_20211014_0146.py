# Generated by Django 2.2.20 on 2021-10-14 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0158_auto_20211012_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='input_json',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='job',
            name='output_playbook',
            field=models.TextField(blank=True, default=''),
        ),
    ]
