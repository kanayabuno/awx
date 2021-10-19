# Generated by Django 2.2.20 on 2021-09-28 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0153_atplaybook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atplaybook',
            name='input_text',
        ),
        migrations.RemoveField(
            model_name='atplaybook',
            name='output_yaml',
        ),
        migrations.AddField(
            model_name='jobtemplate',
            name='input_text',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='jobtemplate',
            name='output_yaml',
            field=models.TextField(blank=True, default=''),
        ),
    ]