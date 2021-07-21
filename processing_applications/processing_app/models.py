from http import client
from django.db import models




class Position(models.Model):
    name = models.CharField(max_length=200)


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    telegram_id = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)



class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    position = models.OneToOneField(Position, on_delete=models.CASCADE)



class TypeApplication(models.Model):
    name = models.CharField(max_length=200)

class StatusApplication(models.Model):
    name = models.CharField(max_length=200)

class Application(models.Model):
    date_created = models.DateField()
    status = models.OneToOneField(StatusApplication, on_delete=models.DO_NOTHING)
    type = models.OneToOneField(TypeApplication, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='applications'                               )
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='applications' )
    description = models.TextField()


