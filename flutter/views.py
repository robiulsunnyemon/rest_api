from django.shortcuts import render
from .models import Teacher,Article
from .serializers import TeacherSerializer,ArticleSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.


def teacher_info(request):
    #complext data
    t=Teacher.objects.all()
    #serializer data
    serializer=TeacherSerializer(t,many=True)
    #serializer data
    json_data=JSONRenderer().render(serializer.data)
    #Json sent to User
    return HttpResponse(json_data,content_type='application/json')


def teacher_info_ins(request,pk):
    #complext data
    t=Teacher.objects.get(id=pk)
    #serializer data
    serializer=TeacherSerializer(t)
    #serializer data
    json_data=JSONRenderer().render(serializer.data)
    #Json sent to User
    return HttpResponse(json_data,content_type='application/json')
