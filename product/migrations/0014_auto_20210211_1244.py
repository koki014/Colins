# Generated by Django 3.1.4 on 2021-02-11 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20210106_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimg',
            name='image',
            field=models.ImageField(upload_to='product_images', verbose_name='Resim'),
        ),
    ]
