# Generated by Django 2.0 on 2017-12-19 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0004_auto_20171219_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='monto',
            field=models.IntegerField(default=0),
        ),
    ]
