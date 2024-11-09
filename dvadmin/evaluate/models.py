from django.db import models

from dvadmin.utils.models import CoreModel

table_prefix = "evaluate_"
# Create your models here.
class Scale(CoreModel):
    title = models.CharField(max_length=64, unique=True, verbose_name="量表名称", help_text="量表名称")
    description = models.TextField(verbose_name="量表描述", help_text="量表描述")
    duration = models.IntegerField(default=1, verbose_name="量表时长", help_text="量表时长")
    testCount = models.IntegerField(default=0, verbose_name="测试总人次", help_text="测试总人次")

    class Meta:
        db_table = table_prefix + "scale"
        verbose_name = "量表"
        verbose_name_plural = verbose_name
        ordering = ("-create_datetime",)


class Question(CoreModel):
    text = models.CharField(max_length=64, verbose_name="题目内容", help_text="题目内容")
    type = models.CharField(max_length=64, verbose_name="题目类型", help_text="题目类型")
    scale = models.ForeignKey(
        to="Scale", # 要关联的表名
        verbose_name="所属量表",
        on_delete=models.CASCADE, # 删除关联数据时,当前表关联数据的行为
        related_name='questions',
        db_constraint=False,
        null=True, # 控制列是否能为null
        blank=True, # 控制列是否能为空
        help_text="关联量表",
    )

    class Meta:
        db_table = table_prefix + "question"
        verbose_name = "题目表"
        verbose_name_plural = verbose_name
        ordering = ("-create_datetime",)


class Option(CoreModel):
    text = models.CharField(max_length=64, verbose_name="选项内容", help_text="选项内容")
    score = models.IntegerField(default=1, verbose_name="选项分数", help_text="选项分数")
    question = models.ForeignKey(
        to="Question", # 要关联的表名
        verbose_name="所属题目",
        on_delete=models.CASCADE, # 删除关联数据时,当前表关联数据的行为
        related_name='options',
        db_constraint=False,
        null=False, # 控制列是否能为null
        blank=False, # 控制列是否能为空
        help_text="关联题目",
    )

    class Meta:
        db_table = table_prefix + "option"
        verbose_name = "选项表"
        verbose_name_plural = verbose_name
        ordering = ("create_datetime",)


class Result(CoreModel):
    user_id = models.IntegerField(verbose_name="测试用户", help_text="测试用户")
    answer = models.TextField(verbose_name="作答内容", help_text="作答内容") #将作答内容转为JSON-str存入
    conclusion = models.TextField(verbose_name="结论", help_text="结论")
    scale = models.ForeignKey(
        to="Scale", # 要关联的表名
        verbose_name="所属量表",
        on_delete=models.CASCADE, # 删除关联数据时,当前表关联数据的行为
        db_constraint=False,
        null=True, # 控制列是否能为null
        blank=True, # 控制列是否能为空
        help_text="关联量表",
    )

    class Meta:
        db_table = table_prefix + "result"
        verbose_name = "测试结果表"
        verbose_name_plural = verbose_name
        ordering = ("-create_datetime",)