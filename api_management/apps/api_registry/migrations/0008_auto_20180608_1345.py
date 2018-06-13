# Generated by Django 2.0.1 on 2018-06-08 16:45

from django.db import migrations


def add_missing_cors(apps, _):
    KongApi = apps.get_model('api_registry', 'KongApi')
    KongPluginCors = apps.get_model('api_registry', 'KongPluginCors')

    for kongapi in KongApi.objects.filter(kongplugincors=None):
        KongPluginCors(apidata=kongapi, enabled=False).save()


class Migration(migrations.Migration):
    dependencies = [
        ('api_registry', '0007_kongplugincors'),
    ]

    operations = [
        migrations.RunPython(add_missing_cors),
    ]
