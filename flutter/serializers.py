from rest_framework import serializers
from flutter.models import Teacher,Article

class TeacherSerializer(serializers.Serializer):
    teacher_name=serializers.CharField(max_length=50)
    course_name=serializers.CharField(max_length=50)
    course_duration=serializers.IntegerField()
    seat=serializers.IntegerField()



class ArticleSerializer(serializers.Serializer):
    class Meta:
        model=Article
        fields= '__all__'