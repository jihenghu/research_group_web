# Generated by Django 2.1 on 2019-12-03 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20191203_0720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={'ordering': ('-product',)},
        ),
        migrations.AddField(
            model_name='productimage',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
