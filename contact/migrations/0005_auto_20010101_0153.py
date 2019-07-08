# Generated by Django 2.2.2 on 2001-01-01 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_subscribe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe',
            name='email',
        ),
        migrations.AddField(
            model_name='subscribe',
            name='sub_email',
            field=models.EmailField(blank=True, max_length=100),
        ),
    ]
