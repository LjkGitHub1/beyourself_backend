# Generated by Django 4.2.7 on 2024-10-22 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("evaluate", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="result",
            name="user_id",
            field=models.IntegerField(help_text="测试用户", verbose_name="测试用户"),
        ),
    ]