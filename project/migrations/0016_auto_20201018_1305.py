# Generated by Django 3.1 on 2020-10-18 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_auto_20201018_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='current_qno',
        ),
        migrations.AddField(
            model_name='response',
            name='current_qno',
            field=models.IntegerField(default=1),
        ),
    ]
