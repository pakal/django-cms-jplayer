# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-23 10:20


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Credits',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'credits',
            },
        ),
        migrations.CreateModel(
            name='JPlayer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('autoplay', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Jplayers',
            },
        ),
        migrations.CreateModel(
            name='JPlayerIntermediate',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jplayer.JPlayer', verbose_name='JPlayer')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('mp3_file', models.FileField(upload_to=b'songs/mp3/')),
                ('ogg_file', models.FileField(blank=True, null=True, upload_to=b'songs/ogg/')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='jplayer.Artist')),
                ('credits', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='jplayer.Credits')),
            ],
        ),
        migrations.AddField(
            model_name='jplayer',
            name='songs',
            field=models.ManyToManyField(related_name='players', to='jplayer.Song'),
        ),
    ]
