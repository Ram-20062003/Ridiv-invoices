# Generated by Django 5.0.1 on 2024-01-03 07:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerName', models.CharField(max_length=100)),
                ('Date', models.DateField(auto_now_add=True)),
                ('InvoiceID', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceDetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=100)),
                ('Quantity', models.IntegerField()),
                ('UnitPrice', models.FloatField()),
                ('Price', models.FloatField()),
                ('InvoiceModelID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice_generator.invoicemodel')),
            ],
        ),
    ]
