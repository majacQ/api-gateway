# Generated by Django 2.0.1 on 2019-01-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0012_zipfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsvCompressorTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('logs', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
