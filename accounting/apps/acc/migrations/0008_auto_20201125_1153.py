# Generated by Django 3.1.3 on 2020-11-25 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0007_auto_20201122_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='ending_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='quantity',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='starting_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='type_of_service',
            field=models.CharField(choices=[('Heating', 'Отопление'), ('Water', 'Вода'), ('Electricity', 'Ток')], max_length=50),
        ),
    ]
