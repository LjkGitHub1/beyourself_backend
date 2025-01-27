# Generated by Django 4.2.7 on 2024-11-15 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("system", "0002_users_identity_card"),
    ]

    operations = [
        migrations.AddField(
            model_name="filelist",
            name="file_type",
            field=models.SmallIntegerField(
                blank=True,
                choices=[(0, "图片"), (1, "视频"), (2, "音频"), (3, "其他")],
                default=3,
                help_text="文件类型",
                null=True,
                verbose_name="文件类型",
            ),
        ),
        migrations.AddField(
            model_name="filelist",
            name="upload_method",
            field=models.SmallIntegerField(
                blank=True,
                choices=[(0, "默认上传"), (1, "文件选择器上传")],
                default=0,
                help_text="上传方式",
                null=True,
                verbose_name="上传方式",
            ),
        ),
    ]
