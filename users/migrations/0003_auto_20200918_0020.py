# Generated by Django 3.0.8 on 2020-09-17 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200917_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(blank=True, max_length=30, verbose_name='Нікнейм'),
        ),
    ]
