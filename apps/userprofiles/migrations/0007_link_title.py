# Generated by Django 3.1.3 on 2023-01-14 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0006_auto_20230105_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]