# Generated by Django 5.0 on 2024-01-02 10:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_curriculum_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculum',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curriculum',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
