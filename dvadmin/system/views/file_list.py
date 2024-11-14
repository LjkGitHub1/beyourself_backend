import hashlib
import mimetypes

from django.contrib.messages import success
from rest_framework import serializers
from rest_framework.decorators import action
from twisted.mail.pop3 import successResponse

from application import dispatch
from dvadmin.system.models import FileList
from dvadmin.utils.json_response import DetailResponse
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet


class FileSerializer(CustomModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    def get_url(self, instance):
        # return 'media/' + str(instance.url)
        return instance.file_url or (f'media/{str(instance.url)}')

    class Meta:
        model = FileList
        fields = "__all__"

    def create(self, validated_data):
        print('self.initial_data.get',self.initial_data.get('file'))
        file_engine = dispatch.get_system_config_values("fileStorageConfig.file_engine") or 'local'
        file_backup = dispatch.get_system_config_values("fileStorageConfig.file_backup")
        file = self.initial_data.get('file')
        # if file is None:
        #     print(self.initial_data)
        #     return super().create(self.initial_data)
        file_size = file.size
        # name = self.initial_data.get['name']
        # if self.initial_data.get('name'):
        #     validated_data['name'] = name or str(file)
        validated_data['name'] = str(file)
        validated_data['size'] = file_size
        md5 = hashlib.md5()
        for chunk in file.chunks():
            md5.update(chunk)
        validated_data['md5sum'] = md5.hexdigest()
        validated_data['engine'] = file_engine
        validated_data['mime_type'] = file.content_type
        # if file_engine == 'local':
        #     file_path = 'localhost:8000:/media/'+file.url
        #     validated_data['file_url'] = file_path
        if file_backup:
            validated_data['url'] = file
        if file_engine == 'oss':
            from dvadmin_cloud_storage.views.aliyun import ali_oss_upload
            file_path = ali_oss_upload(file)
            if file_path:
                validated_data['file_url'] = file_path
            else:
                raise ValueError("上传失败")
        elif file_engine == 'cos':
            from dvadmin_cloud_storage.views.tencent import tencent_cos_upload
            file_path = tencent_cos_upload(file)
            if file_path:
                validated_data['file_url'] = file_path
            else:
                raise ValueError("上传失败")
        else:
            validated_data['url'] = file
        print('url', validated_data['url'] )
        # 审计字段
        try:
            request_user = self.request.user
            print('request_user', request_user)
            validated_data['dept_belong_id'] = request_user.dept.id
            validated_data['creator'] = request_user.id
            validated_data['modifier'] = request_user.id
        except:
            pass
        return super().create(validated_data)


class FileViewSet(CustomModelViewSet):
    """
    文件管理接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = FileList.objects.all()
    serializer_class = FileSerializer
    filter_fields = ['name', ]
    permission_classes = []