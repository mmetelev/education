from rest_framework import serializers

from . import models


class DepartamentSerializer(serializers.ModelSerializer):
    total_employee = serializers.IntegerField()
    total_salary = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = models.Departament
        fields = ('id', 'name', 'director', 'total_employee', 'total_salary')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('id', 'name', 'surname', 'patronymic', 'photo', 'position', 'salary', 'departament')
