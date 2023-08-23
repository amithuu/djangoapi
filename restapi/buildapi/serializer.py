from rest_framework import serializers
from .models import CourseList

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseList
        fields = ('id','course_name', 'language', 'prize')