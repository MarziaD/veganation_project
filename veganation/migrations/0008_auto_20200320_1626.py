# Generated by Django 2.2.1 on 2020-03-20 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veganation', '0007_auto_20200320_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='profile_images'),
        ),
    ]
