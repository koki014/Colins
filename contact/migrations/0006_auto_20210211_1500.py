# Generated by Django 3.1.4 on 2021-02-11 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20210211_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50, verbose_name='adı'),
        ),
    ]
