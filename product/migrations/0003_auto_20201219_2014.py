# Generated by Django 3.1.4 on 2020-12-19 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20201219_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_position',
            field=models.CharField(choices=[('up', 'up'), ('down', 'down'), ('m', 'middle'), ('no', 'none')], default='no', max_length=50, verbose_name='is position'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='slug'),
        ),
    ]