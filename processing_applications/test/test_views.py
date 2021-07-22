import pytest
from rest_framework.test import APIClient
from faker import Faker
from processing_app.models import TypeApplication, StatusApplication, Position, Employee, Client, Application
from django.contrib.auth.models import User


faker = Faker()
application_view = '/api_app/application/'
application_detail_view = '/api_app/application/1/'
client_view = '/api_app/client/'
client_detail_view = '/api_app/client/1/'
employee_view = '/api_app/employee/'
employee_detail_view = '/api_app/employee/1/'


@pytest.fixture
def create_data_for_all_test():
    database_dict = dict(
        status = create_list_status_application(),
        type_ = create_list_type_aplication(),
        client = create_list_client(),
        application = create_list_application(),
        employee = create_list_employee(),
        position = create_list_position_application()
    )
    return database_dict


#test application_view

def test_application_view_method_post(db,create_data_for_all_test):
    client = APIClient()
    data = create_data_for_all_test
    create_database_data(data)
    application_data = create_appication_post_data()
    res = client.post(application_view, data=application_data, format='json' )
    assert res.status_code == 201
    assert Application.objects.count() == 11

def test_application_view_method_get(db, create_data_for_all_test):
    client = APIClient()
    data = create_data_for_all_test
    create_database_data(data)
    res = client.get(application_view)
    assert res.status_code == 200
    assert len(res.data) == 10

def test_application_view_method_put(db, create_data_for_all_test):
    client = APIClient()
    data = create_data_for_all_test
    create_database_data(data)
    data = create_application_put_data()
    res = client.put(application_view, data=data, format='json')
    assert res.status_code == 201
    assert Application.objects.get(pk=1).status.name == 'status 1'

def test_application_view_method_delete(db, create_data_for_all_test):
    client = APIClient()
    data = create_data_for_all_test
    create_database_data(data)
    res = client.delete(application_view, data={"id":1}, format='json')
    assert res.status_code == 200
    assert Application.objects.all().count() == 9

# test application_detail_view

def test_application_detai_lview_method_get(db, create_data_for_all_test):
    client = APIClient()
    data = create_data_for_all_test
    create_database_data(data)
    res = client.get(application_detail_view)
    assert res.status_code == 200
    assert res.data['id'] ==1

# test client_view

def test_client_view_method_get(db, create_data_for_all_test):
    client = APIClient()
    data = create_data_for_all_test
    create_database_data(data)
    res = client.get(client_view)
    assert res.status_code == 200
    assert len(res.data) == 10

def test_client_view_method_put(db, create_data_for_all_test):
    client = APIClient()
    data = create_data_for_all_test
    create_database_data(data)
    client_data = create_client_put_data()
    res = client.put(client_view, data=client_data)
    assert res.status_code == 201
    assert Client.objects.get(pk=1).first_name == 'testuser'

def test_client_view_method_delete(db, create_data_for_all_test):
    client = APIClient()
    data = create_data_for_all_test
    create_database_data(data)
    res = client.delete(client_view, data={"id":1}, format='json')
    assert res.status_code == 200

# test client_detail_view

def test_client_detail_view_method_get(db, create_data_for_all_test):
    client = APIClient()
    data = create_data_for_all_test
    create_database_data(data)
    res = client.get(client_detail_view)
    assert res.status_code == 200
    assert res.data['id'] == 1

# test employee_view

def test_employee_view_method_get(db, create_data_for_all_test):
    client = APIClient()
    data = create_data_for_all_test
    create_database_data(data)
    res = client.get(employee_view)
    assert res.status_code == 200
    assert len(res.data) == 10

def test_employee_view_method_put(db, create_data_for_all_test):
    client = APIClient()
    data = create_data_for_all_test
    create_database_data(data)
    employee_data = create_employee_put_data()
    res = client.put(employee_view, data=employee_data, format='json')
    assert res.status_code == 201
    assert Employee.objects.get(pk=1).first_name == 'testemployee'

def test_employee_view_method_post(db, create_data_for_all_test):
    client = APIClient()
    data = create_data_for_all_test
    create_database_data(data)
    employee_data = create_employee_post_data()
    res = client.post(employee_view, data=employee_data, format='json')
    assert res.status_code == 201
    assert Employee.objects.count() == 11

def test_employee_view_method_delete(db, create_data_for_all_test):
    client = APIClient()
    data = create_data_for_all_test
    create_database_data(data)
    res = client.delete(employee_view, data={'id':1}, format='json')
    assert res.status_code == 201
    assert Employee.objects.count() == 9

# test employee_detail_view
def test_employee_detail_view_method_get(db, create_data_for_all_test):
    client = APIClient()
    data = create_data_for_all_test
    create_database_data(data)
    res = client.get(employee_detail_view)
    assert res.status_code == 200
    assert res.data['id'] == 1


# auxiliary function

def create_employee_post_data()-> dict:
    return dict(
        position={ 'name': 'position 1'},
        first_name= 'testemployee',
        last_name= 'test_employee 1',
    )

def create_employee_put_data() -> dict:
    data = create_employee_post_data()
    data['id'] = 1
    return data


def create_client_post_data()-> dict:
    return dict(

        first_name='testuser',
        last_name = 'testuser 1',

    )

def create_client_put_data()->dict:
    data = create_client_post_data()
    data['id'] =1
    return data

def create_appication_post_data() -> dict:
    return dict(
        status = {'name':'status 1'},
        employee_id = 1,
        client_id = 2,
        type =  {'name':'type 2'},
        description = faker.text(),
    )
def create_application_put_data() -> dict:
    data = create_appication_post_data()
    data['id'] = 1

    return data

def create_database_data( data_for_create: dict) -> None:

    status_list =  data_for_create['status']
    for status in status_list: StatusApplication.objects.create(**status)
    type_list = data_for_create['type_']
    for type_ in  type_list: TypeApplication.objects.create(**type_)
    position_list = data_for_create['position']
    for position in position_list: Position.objects.create(**position) 
    client_list  = data_for_create['client']
    for client in client_list: Client.objects.create(**client)
    employee_list = data_for_create['employee']
    for employee in employee_list: create_employee_in_db(employee)
    application_list = data_for_create['application']
    for application in application_list: create_application_in_db(application)
    User.objects.create(username='testuser', password='testpass')
    
    return

def create_employee_in_db(employee_data : dict):
    position = employee_data['position']
    pos_obj = Position.objects.get(pk=position)
    employee_data['position'] = pos_obj
    Employee.objects.create(**employee_data)
    return

def create_application_in_db(application_data:dict):
    status = application_data['status']
    type_ =  application_data['type']
    client = application_data['client']
    employee = application_data['employee']
    status_obj = StatusApplication.objects.get(pk =status)
    type_obj = TypeApplication.objects.get(pk = type_)
    client_obj = Client.objects.get(pk=client)
    employee_obj = Employee.objects.get(pk=employee)
    application_data['status'] = status_obj 
    application_data['type'] = type_obj
    application_data['client'] = client_obj
    application_data['employee'] = employee_obj
    Application.objects.create(**application_data)
    return

def create_list_type_aplication() -> list:
    list_type = list() 

    for i in range(10):
        type_dict = dict(
            name=f'type {i}'
        )
        
        list_type.append(type_dict)
    return list_type

def create_list_status_application() -> list:
    list_status = list()

    for i in range(10):
        status_dict = dict(
            name = f'status {i}'
        )
        list_status.append(status_dict)
    
    return list_status

def create_list_position_application() -> list:
    list_position = list()

    for i in range(10):
        position_dict = dict(
            name= f'position {i}'
        )
        list_position.append(position_dict)
    return list_position


def create_list_client() -> list:
    list_client = list()
    for i in range(10):
        client_dict = dict(
            first_name = f'name {i}',
            last_name = f'last {i}'

        )
        list_client.append(client_dict)
    return list_client
    
def create_list_employee() -> list:
    list_employee = list()
    for i in range(10):
        employee_dict = dict(
                first_name = 'name_emp_{i}',
                last_name = 'last_emp_{i}',
                position = 1 if i % 2 ==0 else 2
        )
        list_employee.append(employee_dict)
    return list_employee

def create_list_application() -> list:
    list_application = list()
    for i in range(10):
        application_dict = dict(
            status = 1 if i % 2 ==0 else 2,
            type = 1 if i % 2 ==0 else 2,
            client = 1 if i % 2 ==0 else 2,
            employee = 1 if i % 2 ==0 else 2,
            description = faker.text()

        )
        list_application.append(application_dict)
    return list_application