# Generated by Django 3.0.7 on 2020-06-15 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200615_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(default='', max_length=100, verbose_name='Название категории'),
        ),
    ]
