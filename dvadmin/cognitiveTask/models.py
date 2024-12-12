from django.db import models

from dvadmin.utils.models import CoreModel

table_prefix = "cognitive_"
# Create your models here.
class Task(CoreModel):
    title = models.CharField(max_length=64, unique=True, verbose_name="任务名称", help_text="任务名称")
    type = models.CharField(max_length=64, verbose_name="任务类型", help_text="任务类型")
    description = models.TextField(verbose_name="任务描述", help_text="任务描述")
    optip = models.TextField(verbose_name="操作提示", help_text="操作提示")
    duration = models.IntegerField(default=1, verbose_name="预估测试时间", help_text="预估测试时间")
    cover = models.CharField(max_length=64, verbose_name="任务封面", help_text="任务封面")
    testCount = models.IntegerField(default=0, verbose_name="测试总人次", help_text="测试总人次")

    class Meta:
        db_table = table_prefix + "task"
        verbose_name = "认知任务"
        verbose_name_plural = verbose_name
        ordering = ("-create_datetime",)
