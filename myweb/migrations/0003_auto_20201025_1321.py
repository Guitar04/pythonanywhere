# Generated by Django 2.2.7 on 2020-10-25 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0002_auto_20201025_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='offer',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='price',
        ),
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.CharField(max_length=300),
        ),
    ]