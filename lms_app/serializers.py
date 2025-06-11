from rest_framework import serializers
from .models import CourseList,InstructorProfile,StudentRecord,SponsershipDetail


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseList
        fields = ['id','name','description','instructor','difficulty_level']

class InstructorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorProfile 
        fields = ['id','InstructorName','bio'] 
        
class StudentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRecord 
        fields = ['id','name','course']
        
class SponsershipDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsershipDetail
        fields = ['id','students','status','progress']
