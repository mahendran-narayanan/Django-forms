# Generated by Django 3.0.5 on 2020-04-27 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_data_res'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='res',
            new_name='sal',
        ),
    ]
