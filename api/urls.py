
from django.contrib import admin
from django.urls import path,include
from flutter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teacher/',views.teacher_info),
    path('teacher/<int:pk>',views.teacher_info_ins)
]
