# Generated by Django 2.2.3 on 2020-03-31 17:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('veganation', '0025_auto_20200331_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='date1',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='location',
            name='date2',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='location',
            name='date3',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='veganSince',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
