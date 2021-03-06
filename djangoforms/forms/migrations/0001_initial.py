# Generated by Django 3.0.5 on 2020-04-26 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('billing_number', models.BigIntegerField(primary_key=True, serialize=False)),
                ('customer', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('purchase_date', models.DateTimeField()),
                ('company', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('serial_number', models.BigIntegerField()),
                ('mfg_date', models.DateTimeField()),
                ('shipping_date', models.DateTimeField()),
            ],
        ),
    ]
