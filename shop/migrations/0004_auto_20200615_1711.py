# Generated by Django 3.0.7 on 2020-06-15 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='products',
            new_name='product',
        ),
    ]
