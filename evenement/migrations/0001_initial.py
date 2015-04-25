# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('date_event', models.DateField()),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('duree', models.CharField(max_length=256)),
                ('lieu', models.CharField(max_length=256)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('adresse', models.TextField()),
                ('created_at', models.DateField(auto_now=True)),
                ('update_at', models.DateField(auto_now=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
