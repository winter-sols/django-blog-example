# Generated by Django 2.0.2 on 2018-02-19 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180219_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]