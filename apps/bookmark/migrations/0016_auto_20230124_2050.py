# Generated by Django 3.1.3 on 2023-01-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0015_auto_20230111_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='bookmark',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='post_views', to='bookmark.Ip'),
        ),
    ]