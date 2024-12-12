from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-

from rest_framework.response import Response

from dvadmin.cognitiveTask.models import Task
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet



# class ScaleCreateUpdateSerializer(CustomModelSerializer):
#     """
#     认知任务 创建/更新时的列化器
#     """
#
#     class Meta:
#         model = Scale
#         fields = '__all__'

class TaskSerializer(CustomModelSerializer):
    """
    量表-序列化器
    """
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["id"]

class TaskViewSet(CustomModelViewSet):
    """
    认知任务列表接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # create_serializer_class = TaskCreateUpdateSerializer
    # update_serializer_class = TaskCreateUpdateSerializer
    extra_filter_class = []
    search_fields = ['title']


class TaskDataAPIView(CustomModelViewSet):
    """
    量表中的题和选项
    """
    # serializer_class = ScaleSerializer
    @staticmethod
    def get(request, scale_id):
        try:
            task = Task.objects.select_related().prefetch_related('questions__options').get(id = scale_id)
            serializer = TaskSerializer(task)
            return Response(serializer)
        except Task.DoesNotExist:
            return Response({'error': '该认知任务不存在'}, status = 404)