# Generated by Django 2.2.2 on 2001-01-01 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0006_comment_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='name',
        ),
    ]