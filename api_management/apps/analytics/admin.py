from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

from .models import Query


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ['host', 'uri', 'ip_address', 'querystring', 'start_time']


TokenAdmin.raw_id_fields = ('user',)
