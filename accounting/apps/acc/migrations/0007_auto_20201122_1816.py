# Generated by Django 3.1.3 on 2020-11-22 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0006_auto_20201122_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
