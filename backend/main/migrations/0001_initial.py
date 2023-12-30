# Generated by Django 5.0 on 2023-12-29 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('studentId', models.CharField(max_length=20, unique=True)),
                ('course', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('sex', models.CharField(max_length=10)),
                ('contactno', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('citizenship', models.CharField(blank=True, max_length=50, null=True)),
                ('middlename', models.CharField(blank=True, max_length=100, null=True)),
                ('extension', models.CharField(blank=True, max_length=10, null=True)),
                ('birthplace', models.CharField(blank=True, max_length=255, null=True)),
                ('civilstatus', models.CharField(blank=True, max_length=50, null=True)),
                ('religion', models.CharField(blank=True, max_length=100, null=True)),
                ('province', models.CharField(blank=True, max_length=100, null=True)),
                ('municipality', models.CharField(blank=True, max_length=100, null=True)),
                ('brgy', models.CharField(blank=True, max_length=100, null=True)),
                ('postal', models.CharField(blank=True, max_length=20, null=True)),
                ('fatherName', models.CharField(blank=True, max_length=100, null=True)),
                ('fatherOccupation', models.CharField(blank=True, max_length=100, null=True)),
                ('fatherContactNo', models.CharField(blank=True, max_length=20, null=True)),
                ('motherName', models.CharField(blank=True, max_length=100, null=True)),
                ('motherOccupation', models.CharField(blank=True, max_length=100, null=True)),
                ('motherContactNo', models.CharField(blank=True, max_length=20, null=True)),
                ('guardianName', models.CharField(blank=True, max_length=100, null=True)),
                ('guardianOccupation', models.CharField(blank=True, max_length=100, null=True)),
                ('guardianContactNo', models.CharField(blank=True, max_length=20, null=True)),
                ('emergencyContactPerson', models.CharField(blank=True, max_length=100, null=True)),
                ('emergencyRelationship', models.CharField(blank=True, max_length=100, null=True)),
                ('emergencyContactNo', models.CharField(blank=True, max_length=20, null=True)),
                ('juniorHighSchoolName', models.CharField(blank=True, max_length=100, null=True)),
                ('juniorHighSchoolAddress', models.CharField(blank=True, max_length=255, null=True)),
                ('juniorHighSchoolDates', models.CharField(blank=True, max_length=50, null=True)),
                ('seniorHighSchoolName', models.CharField(blank=True, max_length=100, null=True)),
                ('seniorHighSchoolAddress', models.CharField(blank=True, max_length=255, null=True)),
                ('seniorHighSchoolTrack', models.CharField(blank=True, max_length=100, null=True)),
                ('seniorHighSchoolStrand', models.CharField(blank=True, max_length=100, null=True)),
                ('seniorHighSchoolDates', models.CharField(blank=True, max_length=50, null=True)),
                ('vocationalCourseName', models.CharField(blank=True, max_length=100, null=True)),
                ('vocationalSchoolName', models.CharField(blank=True, max_length=100, null=True)),
                ('vocationalCourseDates', models.CharField(blank=True, max_length=50, null=True)),
                ('collegeName', models.CharField(blank=True, max_length=100, null=True)),
                ('collegeAddress', models.CharField(blank=True, max_length=255, null=True)),
                ('collegeDates', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
