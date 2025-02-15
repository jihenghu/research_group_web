# Generated by Django 2.1 on 2019-11-28 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='image',
        ),
        migrations.AddField(
            model_name='publication',
            name='avator',
            field=models.ImageField(blank=True, upload_to='publications/avator/', verbose_name='封面(期刊截图)'),
        ),
        migrations.AddField(
            model_name='publication',
            name='graph',
            field=models.ImageField(blank=True, upload_to='publications/graph/', verbose_name='图表(多图建议先拼接再上传)'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='abstract',
            field=models.TextField(blank=True, null=True, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='accept',
            field=models.DateField(blank=True, null=True, verbose_name='接收日期(Accepted Date)'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='authors',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='作者(使用逗号隔开)'),
        ),
    ]
