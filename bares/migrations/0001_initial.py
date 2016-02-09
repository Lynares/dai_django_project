# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bares',
            fields=[
                ('id_bar', models.AutoField(serialize=False, primary_key=True)),
                ('n_bar', models.CharField(unique=True, max_length=128)),
                ('direccion', models.CharField(unique=True, max_length=128)),
                ('visitas', models.IntegerField(default=10)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Tapas',
            fields=[
                ('id_tapa', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('votos', models.IntegerField(default=0)),
                ('n_bar', models.ForeignKey(to='bares.Bares')),
            ],
        ),
    ]
