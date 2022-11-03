from django.db import models


class Departament(models.Model):
    name = models.CharField(max_length=50)
    director = models.OneToOneField("Employee", on_delete=models.CASCADE, related_name='director', unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='employee/photo/', blank=True)
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    departament = models.ForeignKey(
        Departament,
        on_delete=models.CASCADE,
        related_name='employee',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Фамилия: {self.surname}, Имя: {self.name}"
