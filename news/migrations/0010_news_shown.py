# Generated by Django 2.1 on 2020-03-13 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20200207_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='shown',
            field=models.CharField(choices=[('Y', '显示'), ('N', '不显示')], default='Y', max_length=1, verbose_name='是否在首页轮播显示'),
        ),
    ]
