# Generated by Django 2.1 on 2019-12-03 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20191203_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.Product'),
        ),
    ]
