# Generated by Django 2.0.1 on 2018-12-27 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0009_auto_20181212_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicatorMetricsRow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('all_queries', models.IntegerField(blank=True, null=True)),
                ('all_mobile', models.IntegerField(blank=True, null=True)),
                ('all_not_mobile', models.IntegerField(blank=True, null=True)),
                ('total_users', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
