from django.db import models
import datetime
from django.db.models import QuerySet, Q
from typing import List, Union


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
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)

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


class ApplicationManager(models.Manager):
    
    def _filter_relation_fields(self,value: str, param: str) -> Union[StatusApplication, TypeApplication, QuerySet]:
        dict_model_name = {'type': TypeApplication, 'status': StatusApplication}
        model = dict_model_name[value]
        try:
            object_ = model.objects.get(name=param)
        except model.DoesNotExist:
            return self.none()
        else:
            return object_


    def _create_right_format_date(self, date : str) -> Union[str, QuerySet]:
        try:
            date_list = date.split('/')
            year = int(date_list[2])
            month = int(date_list[1])
            day = int(date_list[0])
            d = datetime.date(year, month, day)
            d_string = d.strftime('%Y-%m-%d')
        except:
            return self.none()
        else:
            return d_string
        
    def _create_right_format_date_between(self, date: str) -> Union[QuerySet, tuple]:
        try:
            date_list = date.split('-')
            date_start = self._create_right_format_date(date_list[0])
            date_end = self._create_right_format_date(date_list[1])
        except:
            return self.none()
        else:
            return date_start, date_end


    def _type_filter(self,params: dict):
        type_param = params['type']
        type_object = self._filter_relation_fields(value='type', param=type_param)
        return self.filter(type=type_object.pk) if not isinstance(type_object,QuerySet) else type_object
    
    def _status_filter(self, params: dict):
        status_param = params['status']
        status_object = self._filter_relation_fields(value='status', param=status_param)
        return self.filter(status=status_object.pk) if not isinstance(status_object, QuerySet) else status_object
    
    def _statuses_filter(self, params: dict) -> Union[QuerySet, List]:
        begin_queryset = list()
        statuses = params['statuses']
        statuses_list = statuses.split('-')
        for status_param in statuses_list:
            status_object = self._filter_relation_fields(value='status', param=status_param)
            if isinstance(status_object, QuerySet):
                return status_object
            new_queryset = self.filter(status=status_object.pk)
            begin_queryset += new_queryset
        else:
            return begin_queryset
        

    def _date_created_filter(self, params: dict) -> QuerySet:
        date_created = params['date_created']
        date = self._create_right_format_date(date_created)
        if isinstance(date, QuerySet):
            return date
            
        return self.filter(date_created=date)
    
    def _date_created_between_filter(self, params):
        date_created_between = params['date_created_between']
        date_tuple = self._create_right_format_date_between(date_created_between)
        if isinstance(date_tuple, QuerySet):
            return date_tuple
        Q1 = Q(date_created__gte=date_tuple[0])
        Q2 = Q(date_created__gte = date_tuple[1])
        return self.filter(Q1 & Q2)
        

    def filter_params(self, params: dict) -> Union[QuerySet, list]:
        queryset_list = self.all()
        if 'type' in params:
            return self._type_filter(params)
                            
        if 'status' in params:
            return self._status_filter(params)
            
        if 'statuses' in params:
            return self._statuses_filter(params)
        
        if 'date_created' in params:
            return self._date_created_filter(params)
        
        if 'date_created_between' in params:
            return self._date_created_between_filter(params)

        return queryset_list 

class Application(models.Model):
    date_created = models.DateField(auto_now_add=True)
    status = models.ForeignKey(StatusApplication, on_delete=models.DO_NOTHING)
    type = models.ForeignKey(TypeApplication, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='applications')
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='applications' )
    description = models.TextField()
    objects = ApplicationManager()

    def __str__(self) -> str:
        return f'{self.date_created}'


