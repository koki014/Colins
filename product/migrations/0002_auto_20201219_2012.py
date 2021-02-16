# Generated by Django 3.1.4 on 2020-12-19 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_position',
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='slug'),
        ),
    ]
