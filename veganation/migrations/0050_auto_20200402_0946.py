# Generated by Django 2.2.1 on 2020-04-02 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veganation', '0049_auto_20200402_0942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='date2',
        ),
        migrations.RemoveField(
            model_name='location',
            name='date3',
        ),
    ]
