# Generated by Django 2.1 on 2019-11-28 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0003_auto_20191128_0944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='avator',
            new_name='avatar',
        ),
    ]
