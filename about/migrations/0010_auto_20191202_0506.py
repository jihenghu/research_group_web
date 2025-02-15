# Generated by Django 2.1 on 2019-12-02 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_auto_20191130_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='biography',
            field=models.TextField(blank=True, null=True, verbose_name='个人简介'),
        ),
        migrations.AlterField(
            model_name='member',
            name='honor',
            field=models.TextField(blank=True, null=True, verbose_name='荣誉和奖项'),
        ),
        migrations.AlterField(
            model_name='member',
            name='interests',
            field=models.TextField(blank=True, null=True, verbose_name='研究领域'),
        ),
        migrations.AlterField(
            model_name='member',
            name='nowwhere',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='何地从事'),
        ),
        migrations.AlterField(
            model_name='member',
            name='project',
            field=models.TextField(blank=True, null=True, verbose_name='主持项目'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='简单说明'),
        ),
    ]
