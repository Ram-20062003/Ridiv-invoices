# Generated by Django 5.0.1 on 2024-01-07 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_generator', '0003_alter_invoicedetailmodel_invoicemodelid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicemodel',
            name='InvoiceID',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
