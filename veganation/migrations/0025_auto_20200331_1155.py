# Generated by Django 2.2.1 on 2020-03-31 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veganation', '0024_auto_20200331_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='age',
            field=models.IntegerField(default=5),
        ),
    ]
