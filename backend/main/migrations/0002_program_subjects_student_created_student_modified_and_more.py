# Generated by Django 5.0 on 2023-12-30 05:15

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('units', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('prereq', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('effectivity', models.CharField(max_length=100)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.program')),
            ],
        ),
        migrations.CreateModel(
            name='Prospectus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('semester', models.CharField(max_length=100)),
                ('yrlevel', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.curriculum')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subjects')),
            ],
        ),
    ]
