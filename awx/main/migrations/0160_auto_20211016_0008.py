# Generated by Django 2.2.20 on 2021-10-16 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0159_auto_20211014_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='input_json',
            field=models.TextField(blank=True, default='{}'),
        ),
        migrations.AlterField(
            model_name='jobtemplate',
            name='input_json',
            field=models.TextField(blank=True, default='{}'),
        ),
    ]
