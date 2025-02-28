# Generated by Django 2.0.1 on 2018-04-17 13:24

import api_management.apps.api_registry.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KongApi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=False)),
                ('kong_id', models.UUIDField(null=True)),
                ('name', models.CharField(max_length=200, unique=True, validators=[api_management.apps.api_registry.validators.AlphanumericValidator()])),
                ('upstream_url', models.URLField()),
                ('hosts', models.CharField(blank=True, default='', max_length=200, validators=[api_management.apps.api_registry.validators.HostsValidator()])),
                ('uri', models.CharField(blank=True, default='', max_length=200, validators=[api_management.apps.api_registry.validators.UrisValidator()])),
                ('strip_uri', models.BooleanField(default=True)),
                ('preserve_host', models.BooleanField(default=False)),
                ('documentation_url', models.URLField(blank=True)),
                ('docs_kong_id', models.UUIDField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KongPluginHttpLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=False)),
                ('kong_id', models.UUIDField(null=True)),
                ('api_key', models.CharField(max_length=100)),
                ('exclude_regex', models.CharField(blank=True, max_length=100)),
                ('apidata', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api_registry.KongApi')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KongPluginJwt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=False)),
                ('kong_id', models.UUIDField(null=True)),
                ('apidata', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api_registry.KongApi')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KongPluginRateLimiting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=False)),
                ('kong_id', models.UUIDField(null=True)),
                ('second', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('minute', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('hour', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('day', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('apidata', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api_registry.KongApi')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TokenRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=254)),
                ('consumer_application', models.CharField(max_length=200)),
                ('requests_per_day', models.IntegerField()),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_registry.KongApi')),
            ],
        ),
    ]
