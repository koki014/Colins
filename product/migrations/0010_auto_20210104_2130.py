# Generated by Django 3.1.4 on 2021-01-04 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20210104_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimg',
            name='image',
            field=models.ImageField(upload_to='product_images', verbose_name='Resim'),
        ),
    ]
