# Generated by Django 3.1.3 on 2022-12-27 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0008_auto_20221227_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='count',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='visits',
            field=models.IntegerField(default=0),
        ),
    ]
