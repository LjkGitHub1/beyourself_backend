from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-


from django.db.models import F
from rest_framework.response import Response
from rest_framework.views import APIView

from dvadmin.evaluate.models import Scale, Question, Option, Result
from rest_framework.decorators import action

from dvadmin.system.models import RoleMenuPermission, Menu, MenuButton
from dvadmin.utils.json_response import DetailResponse, ErrorResponse
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet



# class ScaleCreateUpdateSerializer(CustomModelSerializer):
#     """
#     量表 创建/更新时的列化器
#     """
#
#     class Meta:
#         model = Scale
#         fields = '__all__'

class ResultSerializer(CustomModelSerializer):
    """
    测试结果-序列化器
    """

    class Meta:
        model = Result
        fields = "__all__"
        read_only_fields = ["id"]

class OptionSerializer(CustomModelSerializer):
    """
    选项-序列化器
    """

    class Meta:
        model = Option
        fields = "__all__"
        read_only_fields = ["id"]


class QuestionSerializer(CustomModelSerializer):
    """
    题目-序列化器
    """
    # 注意顺序，需在字表的后边定义该序列化,
    # 属性与子表的related_name对应
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = "__all__"
        read_only_fields = ["id"]

class ScaleSerializer(CustomModelSerializer):
    """
    量表-序列化器
    """
    questions = QuestionSerializer(many=True)
    class Meta:
        model = Scale
        fields = "__all__"
        read_only_fields = ["id"]

class QuestionViewSet(CustomModelViewSet):
    """
    题目接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # create_serializer_class = ScaleCreateUpdateSerializer
    # update_serializer_class = ScaleCreateUpdateSerializer
    extra_filter_class = []
    search_fields = ['text']

class OptionViewSet(CustomModelViewSet):
    """
    选项接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    # create_serializer_class = ScaleCreateUpdateSerializer
    # update_serializer_class = ScaleCreateUpdateSerializer
    extra_filter_class = []
    search_fields = ['text']

class ResultViewSet(CustomModelViewSet):
    """
    测试结果接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Option.objects.all()
    serializer_class = ResultSerializer
    # create_serializer_class = ScaleCreateUpdateSerializer
    # update_serializer_class = ScaleCreateUpdateSerializer
    extra_filter_class = []
    search_fields = ['user_id']

class ScaleViewSet(CustomModelViewSet):
    """
    量表接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Scale.objects.all()
    serializer_class = ScaleSerializer
    # create_serializer_class = ScaleCreateUpdateSerializer
    # update_serializer_class = ScaleCreateUpdateSerializer
    extra_filter_class = []
    search_fields = ['title']

class ScaleDataAPIView(CustomModelViewSet):
    """
    量表中的题和选项
    """
    # serializer_class = ScaleSerializer
    @staticmethod
    def get(request, scale_id):
        try:
            scale = Scale.objects.select_related().prefetch_related('questions__options').get(id = scale_id)
            serializer = ScaleSerializer(scale)
            return Response(serializer)
        except Scale.DoesNotExist:
            return Response({'error': '该量表不存在'}, status = 404)