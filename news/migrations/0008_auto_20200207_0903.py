# Generated by Django 2.1 on 2020-02-07 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20200207_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='avatar',
            field=models.ImageField(null=True, upload_to='news/avatar/%Y%m%d/', verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to='news/image/%Y%m%d/', verbose_name='文中图(多图建议先拼接再上传)'),
        ),
    ]
