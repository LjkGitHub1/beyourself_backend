from django.urls import path
from rest_framework import routers

from dvadmin.cognitiveTask.views.task import TaskViewSet

system_url = routers.SimpleRouter()
system_url.register(r'task', TaskViewSet, basename='cognitive')

urlpatterns = [
    path('task/', TaskViewSet.as_view({'get': 'list','post': 'create'})),
    # path('task/data/<int:task_id>/', TaskDataAPIView.as_view({'get':'list'}),name='task_data'),
    # path('task/question/', QuestionViewSet.as_view({'get': 'list','post': 'create'})),
]
urlpatterns += system_url.urls
