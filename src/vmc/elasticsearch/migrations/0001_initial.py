# Generated by Django 2.2.9 on 2020-02-21 19:46

from django.db import migrations, models
import django.db.models.deletion


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
                ('prefix', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'elasticsearch_config',
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('slug_name', models.CharField(max_length=128)),
                ('elasticsearch_config', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='elasticsearch.Config')),
            ],
            options={
                'db_table': 'elasticsearch_tenant',
            },
        ),
        migrations.CreateModel(
            name='DocumentRegistry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('index_name', models.CharField(max_length=256)),
                ('module', models.CharField(max_length=256)),
                ('document', models.CharField(max_length=256)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='elasticsearch.Tenant')),
            ],
            options={
                'db_table': 'elasticsearch_document_registry',
            },
        ),
    ]