# Generated by Django 2.2.20 on 2021-10-12 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0156_auto_20211012_0019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atplaybook',
            options={'base_manager_name': 'objects'},
        ),
        migrations.RemoveField(
            model_name='atplaybook',
            name='input_text',
        ),
        migrations.RemoveField(
            model_name='atplaybook',
            name='output_yaml',
        ),
    ]
