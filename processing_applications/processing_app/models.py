from http import client
from django.db import models




class Position(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name



class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    telegram_id = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"



class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    position = models.OneToOneField(Position, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"



class TypeApplication(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class StatusApplication(models.Model):
    name = models.CharField(max_length=200)
    

    def __str__(self) -> str:
        return self.name

class Application(models.Model):
    date_created = models.DateField(auto_now_add=True)
    statuses = models.ManyToManyField(StatusApplication)
    type = models.ForeignKey(TypeApplication, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='applications'                               )
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='applications' )
    description = models.TextField()

    def __str__(self) -> str:
        return f'{self.date_created}'


