# Generated by Django 2.0.1 on 2018-10-25 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0007_googleanalyticssettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiSessionSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_timeout', models.IntegerField(default=10, verbose_name='Timeout in minutes')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
