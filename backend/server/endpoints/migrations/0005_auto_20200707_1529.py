# Generated by Django 2.2.4 on 2020-07-07 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0004_auto_20200706_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='symptoms',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='symptoms',
            name='lastname',
        ),
    ]
