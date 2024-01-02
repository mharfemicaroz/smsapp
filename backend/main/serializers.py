from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'

class CurriculumSerializer(serializers.ModelSerializer):
    program_data = ProgramSerializer(source='program', read_only=True)
    class Meta:
        model = Curriculum
        fields = '__all__'

class ProspectusSerializer(serializers.ModelSerializer):
    curriculum_data = CurriculumSerializer(source='curriculum', read_only=True)
    subject_data = SubjectsSerializer(source='subject', read_only=True)
    class Meta:
        model = Prospectus
        fields = '__all__'