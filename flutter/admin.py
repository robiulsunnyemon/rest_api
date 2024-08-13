from django.contrib import admin
from .models import Teacher,Article

# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["teacher_name", "course_name", "course_duration","seat"]
    

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "body"]
    