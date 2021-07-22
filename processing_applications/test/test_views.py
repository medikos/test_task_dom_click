import pytest
from rest_framework.test import APIClient
from faker import Faker
from processing_app.models import TypeApplication, StatusApplication, Position, Employee, Client, Application
from django.contrib.auth.models import User


faker = Faker()
application_view = '/api_app/application/'




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

def test_application_view_method_delete():
    pass

# test application_detail_view

def test_application_detai_lview_method_get():
    pass

# test client_view

def test_client_view_method_get():
    pass

def test_client_view_method_put():
    pass

def test_client_view_method_delete():
    pass

# test client_detail_view

def test_client_detail_view_method_get():
    pass

# test employee_view

def test_employee_view_method_get():
    pass

def test_employee_view_method_put():
    pass

def test_employee_view_method_post():
    pass

def test_employee_view_method_delete():
    pass


# test employee_detail_view
def test_employee_detail_view_method_get():
    pass



# auxiliary function

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