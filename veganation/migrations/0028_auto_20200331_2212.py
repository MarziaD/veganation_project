# Generated by Django 2.2.3 on 2020-03-31 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veganation', '0027_auto_20200331_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='myaccount', to=settings.AUTH_USER_MODEL),
        ),
    ]
