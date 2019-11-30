# Generated by Django 2.2.4 on 2019-11-30 15:23

import vmc.common.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('url', models.CharField(max_length=128)),
                ('api_key', models.TextField()),
                ('secret_key', models.TextField()),
                ('insecure', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, vmc.common.models.ModelDiffMixin),
        ),
    ]