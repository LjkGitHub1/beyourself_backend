# Generated by Django 4.2.7 on 2024-11-04 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("evaluate", "0005_option_score_alter_option_question"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="option",
            options={
                "ordering": ("create_datetime",),
                "verbose_name": "选项表",
                "verbose_name_plural": "选项表",
            },
        ),
        migrations.AlterField(
            model_name="option",
            name="question",
            field=models.ForeignKey(
                db_constraint=False,
                help_text="关联题目",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="options",
                to="evaluate.question",
                verbose_name="所属题目",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="scale",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                help_text="关联量表",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="evaluate.scale",
                verbose_name="所属量表",
            ),
        ),
    ]
