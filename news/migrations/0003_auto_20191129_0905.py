# Generated by Django 2.1 on 2019-11-29 09:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20191129_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='时间'),
        ),
    ]
