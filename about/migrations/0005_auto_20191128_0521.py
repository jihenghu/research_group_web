# Generated by Django 2.1 on 2019-11-28 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20191128_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='title',
            field=models.CharField(blank=True, choices=[('professor', '教授'), ('postdoc', '博士后'), ('phd', '博士研究生'), ('graduate', '硕士研究生'), ('under', '本科生'), ('visit', '访问/交流')], max_length=20, null=True, verbose_name='头衔'),
        ),
    ]
