# Generated by Django 5.0 on 2024-01-02 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_program_subjects_student_created_student_modified_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='description',
            new_name='longname',
        ),
        migrations.AddField(
            model_name='program',
            name='major',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
