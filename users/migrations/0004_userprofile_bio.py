# Generated by Django 3.0.8 on 2020-10-31 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200918_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, verbose_name='Біографія'),
        ),
    ]
