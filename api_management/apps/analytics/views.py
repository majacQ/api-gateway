
from django.http import HttpResponse
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.pagination import CursorPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters

from api_management.apps.analytics import swaggers
from api_management.apps.analytics.csv_generator import CsvGenerator
from .models import Query, CsvFile
from .serializers import QuerySerializer
from .tasks import make_model_object
from .filters import QueryFilter


class QueryViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    class CustomPagination(CursorPagination):
        page_size = 1000

    pagination_class = CustomPagination
    filter_backends = [
        filters.DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_class = QueryFilter
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    permission_classes = [IsAdminUser, ]
    authentication_classes = [TokenAuthentication, ]
    ordering_fields = ('id', 'start_time', 'request_time', )
    ordering = ('id', )

    def create(self, request, *args, **kwargs):
        super(QueryViewSet, self).create(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        make_model_object.delay(serializer.data, type(serializer))


@api_view(['GET'])
def query_swagger_view(*_, **__):
    return Response(swaggers.QUERIES)


@api_view(['GET'])
def download_csv_view(request, api_name, date):
    response = HttpResponse()

    files = CsvFile.objects.filter(api_name=api_name, file_name=f'analytics_{date}.csv')
    if files.exists() and files.first().file is not None:
        response['Content-Disposition'] = f"attachment; filename='{date}'"
        response.content_type = 'text/csv'
        response.content = files.first().file
    else:
        response.status_code = 501
    return response


@api_view(['GET'])
def generate_csv_view(request, api_name, date):
    csv_generator = CsvGenerator(api_name=api_name, date=date)
    csv_generator.generate()