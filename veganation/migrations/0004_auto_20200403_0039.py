# Generated by Django 2.2.3 on 2020-04-02 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veganation', '0003_auto_20200402_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='veganSince',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]