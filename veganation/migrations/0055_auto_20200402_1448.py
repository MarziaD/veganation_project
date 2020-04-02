# Generated by Django 2.2.3 on 2020-04-02 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veganation', '0054_merge_20200402_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='id',
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=128, primary_key=True, serialize=False, unique=True),
        ),
    ]