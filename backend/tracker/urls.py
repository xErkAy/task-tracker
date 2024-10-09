from django.conf.urls.static import static
from django.urls import path, include, re_path
from tracker import views

urlpatterns = [
    re_path('api/tasks/$', views.TaskListAPIView.as_view()),
    re_path('api/tasks/info/$', views.TaskInfoAPIView.as_view()),
    re_path('api/tasks/(?P<id>\d+)/$', views.TaskDetailAPIView.as_view()),
]
