# Generated by Django 4.2.7 on 2024-12-12 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        help_text="Id",
                        primary_key=True,
                        serialize=False,
                        verbose_name="Id",
                    ),
                ),
                (
                    "modifier",
                    models.CharField(
                        blank=True,
                        help_text="修改人",
                        max_length=255,
                        null=True,
                        verbose_name="修改人",
                    ),
                ),
                (
                    "dept_belong_id",
                    models.CharField(
                        blank=True,
                        help_text="数据归属部门",
                        max_length=255,
                        null=True,
                        verbose_name="数据归属部门",
                    ),
                ),
                (
                    "update_datetime",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="修改时间",
                        null=True,
                        verbose_name="修改时间",
                    ),
                ),
                (
                    "create_datetime",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="创建时间",
                        null=True,
                        verbose_name="创建时间",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="任务名称",
                        max_length=64,
                        unique=True,
                        verbose_name="任务名称",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        help_text="任务类型", max_length=64, verbose_name="任务类型"
                    ),
                ),
                (
                    "description",
                    models.TextField(help_text="任务描述", verbose_name="任务描述"),
                ),
                (
                    "optip",
                    models.TextField(help_text="操作提示", verbose_name="操作提示"),
                ),
                (
                    "duration",
                    models.IntegerField(
                        default=1, help_text="预估测试时间", verbose_name="预估测试时间"
                    ),
                ),
                (
                    "cover",
                    models.CharField(
                        help_text="任务封面", max_length=64, verbose_name="任务封面"
                    ),
                ),
                (
                    "testCount",
                    models.IntegerField(
                        default=0, help_text="测试总人次", verbose_name="测试总人次"
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        db_constraint=False,
                        help_text="创建人",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_query_name="creator_query",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="创建人",
                    ),
                ),
            ],
            options={
                "verbose_name": "认知任务",
                "verbose_name_plural": "认知任务",
                "db_table": "cognitive_task",
                "ordering": ("-create_datetime",),
            },
        ),
    ]