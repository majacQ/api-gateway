# Generated by Django 2.0.1 on 2018-08-21 19:47

import api_management.apps.api_registry.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_registry', '0011_add_missing_jwt_anonymous_consumer'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='kongconsumer',
            managers=[
                ('objects', api_management.apps.api_registry.models.KongConsumerManager()),
            ],
        ),
    ]
