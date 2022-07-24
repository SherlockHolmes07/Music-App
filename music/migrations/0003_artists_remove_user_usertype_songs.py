# Generated by Django 4.0.5 on 2022-07-24 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_user_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('artist_photo', models.URLField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='userType',
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('song_file', models.FileField(upload_to='songs/')),
                ('image_url', models.URLField(blank=True, max_length=500)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_songs', to='music.artists')),
            ],
        ),
    ]