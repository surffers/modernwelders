# Generated by Django 3.1.3 on 2023-01-11 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmark', '0014_auto_20230105_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='number_of_votes',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='bookmark.bookmark')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]