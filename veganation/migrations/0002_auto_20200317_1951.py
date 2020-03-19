# Generated by Django 3.0.3 on 2020-03-17 19:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('veganation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='picture',
            new_name='profilePic',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='veganation@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='firstName',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='isVegan',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastName',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='occupation',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='quote',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='veganSince',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
