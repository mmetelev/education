from django.contrib.auth.models import User

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from . import models


class WorkerTests(APITestCase):

    def setUp(self) -> None:
        user = User.objects.create_superuser(username='test', email='testuser@test.com', password='test')
        user.save()

        self.token = Token.objects.create(user=user)
        self.token.save()

        employee_dir = models.Employee.objects.create(
            id=1,
            name='Устинов',
            surname='Даниэль',
            patronymic='Давидович',
            position='Директор',
            salary='10000',
        )

        departament = models.Departament.objects.create(
            name='Бухгалтерия',
            director=employee_dir,
        )

        self.employee = models.Employee.objects.create(
            id=2,
            name='Иван',
            surname='Иванов',
            patronymic='Иванович',
            position='Бухгалтер',
            salary='50000',
            departament=departament
        )

    def test_get_employee(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.get(reverse('employees-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_employee_not_auth(self):
        response = self.client.get(reverse('employees-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_employee(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        data = {
            "name": "Александр",
            "surname": "Баженов",
            "patronymic": "Максимович",
            "position": "Стажер",
            "salary": "10000.00",
        }
        response = self.client.post(reverse('employees-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_employee_not_auth(self):
        data = {
            "name": "Александр",
            "surname": "Баженов",
            "patronymic": "Максимович",
            "position": "Стажер",
            "salary": "10000.00",
        }
        response = self.client.post(reverse('employees-list'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_employee(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.delete(reverse('employees-detail', kwargs={"pk": self.employee.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_departament(self):
        response = self.client.get(reverse('departments'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
