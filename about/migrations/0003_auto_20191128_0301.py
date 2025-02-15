# Generated by Django 2.1 on 2019-11-28 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20191127_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='end',
            field=models.DateField(blank=True, null=True, verbose_name='何日止'),
        ),
        migrations.AddField(
            model_name='member',
            name='nowwhere',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='何地从事'),
        ),
        migrations.AddField(
            model_name='member',
            name='start',
            field=models.DateField(blank=True, null=True, verbose_name='何日始'),
        ),
        migrations.AddField(
            model_name='member',
            name='state',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='在校？'),
        ),
    ]
