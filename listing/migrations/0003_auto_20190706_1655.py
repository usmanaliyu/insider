# Generated by Django 2.2.2 on 2019-07-06 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_auto_20190706_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='country',
            field=models.CharField(max_length=100),
        ),
    ]