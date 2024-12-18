# Generated by Django 4.2.7 on 2024-10-22 23:47

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
            name="Scale",
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
                        help_text="量表名称",
                        max_length=64,
                        unique=True,
                        verbose_name="量表名称",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="量表描述", max_length=64, verbose_name="量表描述"
                    ),
                ),
                (
                    "duration",
                    models.IntegerField(
                        default=1, help_text="量表时长", verbose_name="量表时长"
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
                "verbose_name": "量表",
                "verbose_name_plural": "量表",
                "db_table": "evaluate_scale",
                "ordering": ("-create_datetime",),
            },
        ),
        migrations.CreateModel(
            name="Result",
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
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="描述",
                        max_length=255,
                        null=True,
                        verbose_name="描述",
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
                    "user_id",
                    models.IntegerField(
                        help_text="测试用户", max_length=8, verbose_name="测试用户"
                    ),
                ),
                (
                    "answer",
                    models.TextField(help_text="作答内容", verbose_name="作答内容"),
                ),
                ("conclusion", models.TextField(help_text="结论", verbose_name="结论")),
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
                (
                    "scale_id",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        help_text="关联量表",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="evaluate.scale",
                        verbose_name="所属量表",
                    ),
                ),
            ],
            options={
                "verbose_name": "测试结果表",
                "verbose_name_plural": "测试结果表",
                "db_table": "evaluate_result",
                "ordering": ("-create_datetime",),
            },
        ),
        migrations.CreateModel(
            name="Question",
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
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="描述",
                        max_length=255,
                        null=True,
                        verbose_name="描述",
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
                    "text",
                    models.CharField(
                        help_text="题目内容", max_length=64, verbose_name="题目内容"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        help_text="题目类型", max_length=64, verbose_name="题目类型"
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
                (
                    "scale_id",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        help_text="关联量表",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="evaluate.scale",
                        verbose_name="所属量表",
                    ),
                ),
            ],
            options={
                "verbose_name": "题目表",
                "verbose_name_plural": "题目表",
                "db_table": "evaluate_question",
                "ordering": ("-create_datetime",),
            },
        ),
        migrations.CreateModel(
            name="Option",
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
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="描述",
                        max_length=255,
                        null=True,
                        verbose_name="描述",
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
                    "text",
                    models.CharField(
                        help_text="选项内容", max_length=64, verbose_name="选项内容"
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
                (
                    "question_id",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        help_text="关联题目",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="evaluate.option",
                        verbose_name="所属题目",
                    ),
                ),
            ],
            options={
                "verbose_name": "选项表",
                "verbose_name_plural": "选项表",
                "db_table": "evaluate_option",
                "ordering": ("-create_datetime",),
            },
        ),
    ]
