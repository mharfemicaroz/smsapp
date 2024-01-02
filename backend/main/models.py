from django.db import models

class Program(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1024, null=True, blank=True)
    major = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    units = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    subtype = models.CharField(max_length=100)
    prereq = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Curriculum(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Prospectus(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    semester = models.CharField(max_length=100)
    yrlevel = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Student(models.Model):
    # Required fields
    id = models.AutoField(primary_key=True)
    studentId = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    birthdate = models.DateField()
    sex = models.CharField(max_length=10)
    contactno = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255)

    # Optional fields
    citizenship = models.CharField(max_length=50, null=True, blank=True)
    middlename = models.CharField(max_length=100, null=True, blank=True)
    extension = models.CharField(max_length=10, null=True, blank=True)
    birthplace = models.CharField(max_length=255, null=True, blank=True)
    civilstatus = models.CharField(max_length=50, null=True, blank=True)
    religion = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    municipality = models.CharField(max_length=100, null=True, blank=True)
    brgy = models.CharField(max_length=100, null=True, blank=True)
    postal = models.CharField(max_length=20, null=True, blank=True)
    fatherName = models.CharField(max_length=100, null=True, blank=True)
    fatherOccupation = models.CharField(max_length=100, null=True, blank=True)
    fatherContactNo = models.CharField(max_length=20, null=True, blank=True)
    motherName = models.CharField(max_length=100, null=True, blank=True)
    motherOccupation = models.CharField(max_length=100, null=True, blank=True)
    motherContactNo = models.CharField(max_length=20, null=True, blank=True)
    guardianName = models.CharField(max_length=100, null=True, blank=True)
    guardianOccupation = models.CharField(max_length=100, null=True, blank=True)
    guardianContactNo = models.CharField(max_length=20, null=True, blank=True)
    emergencyContactPerson = models.CharField(max_length=100, null=True, blank=True)
    emergencyRelationship = models.CharField(max_length=100, null=True, blank=True)
    emergencyContactNo = models.CharField(max_length=20, null=True, blank=True)
    juniorHighSchoolName = models.CharField(max_length=100, null=True, blank=True)
    juniorHighSchoolAddress = models.CharField(max_length=255, null=True, blank=True)
    juniorHighSchoolDates = models.CharField(max_length=50, null=True, blank=True)
    seniorHighSchoolName = models.CharField(max_length=100, null=True, blank=True)
    seniorHighSchoolAddress = models.CharField(max_length=255, null=True, blank=True)
    seniorHighSchoolTrack = models.CharField(max_length=100, null=True, blank=True)
    seniorHighSchoolStrand = models.CharField(max_length=100, null=True, blank=True)
    seniorHighSchoolDates = models.CharField(max_length=50, null=True, blank=True)
    vocationalCourseName = models.CharField(max_length=100, null=True, blank=True)
    vocationalSchoolName = models.CharField(max_length=100, null=True, blank=True)
    vocationalCourseDates = models.CharField(max_length=50, null=True, blank=True)
    collegeName = models.CharField(max_length=100, null=True, blank=True)
    collegeAddress = models.CharField(max_length=255, null=True, blank=True)
    collegeDates = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
