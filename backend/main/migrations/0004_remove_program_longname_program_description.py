# Generated by Django 5.0 on 2024-01-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_description_program_longname_program_major'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='longname',
        ),
        migrations.AddField(
            model_name='program',
            name='description',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
    ]
