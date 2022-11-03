from django.db.models import Sum, Count

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import parsers
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from . import models, serializers


class EmployeePagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 10000


class EmployeeView(ModelViewSet):
    queryset = models.Employee.objects.select_related('departament').all()
    serializer_class = serializers.EmployeeSerializer
    parser_classes = [parsers.MultiPartParser]
    permission_classes = [IsAuthenticated]
    pagination_class = EmployeePagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['surname', 'departament']


class DepartamentView(ModelViewSet):
    serializer_class = serializers.DepartamentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return (
            models.Departament.objects
            .annotate(total_salary=Sum('employee__salary'), total_employee=Count('employee'))
            .select_related('director')
            .all()
        )
