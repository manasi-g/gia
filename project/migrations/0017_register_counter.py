# Generated by Django 3.1 on 2020-10-18 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_auto_20201018_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]
