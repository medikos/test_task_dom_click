
### Зависимости
1. django
2. djangorestframework
3. Faker
4. pytest-django
5. djangorestframework-simplejwt

### Описание
CRM сервис на базе REST  позволяет управлять  следить за заявками клиентов, аутенфикация через JWT.
Реализованна панель администратора с удобным интерфейсом.
Есть возможность интеграции с любым приложением за счет реализованного API.

### Панель администратора
     GET /admin/
    
### Аутенфикация
    GET /api/token/ 
    Создание JWT  токена.
    
    GET  /api/token/refresh/
    Обновление JWT токена.
    Для включения уровня разрешений для всего сайта в файл настроек нужно добавить.
    
         REST_FRAMEWORK =   {
        'DEFAULT_PERMISSION_CLASSES':   [
            'rest_framework.permissions.IsAuthenticated',
                ]
                    }

    


### Реализованные обработчики REST API 
  
    POST PUT DELETE GET	 /api_app/application/ 
    Создание, обновление, удаление и просмотр обьектов заявок базе данных, в случае успеха возвращяется код 201 в при некоректных данных код 400.
    Заявки фильтруются через GET параметры:
    
    /api_app/application/?status=open
    /api_app/application/?statuses=open-close
    /api_app/application/?type=repair
    /api_app/application/?date_created=28/02/2021
    /api_app/application/?date_created_between=28/02/2021-15/03/2021
    
    
    Пример POST данных.
    
        {
            employee_id : 1,
            client_id : 1,
            status : "open",
            description: 'Починка стиральной машины',
            type: 'ремонт',
        }
	
    При PUT запросе необходимо добавлять id обьекта в словарь.
  
    Пример DELETE запроса:
        {
            id:1
        }
    
	GET /api_app/application/$id_application/
    Получение заявки по id.
    
    GET POST PUT DELETE /api_app/client/
    Создание, обновление, удаление и просмотр  клиентов в базе данных, в случае успеха возвращяется код 201 в при некоректных данных код 400.
    
    GET /api_app/client/$id_client/
    Получение клиента по id.
    
    GET POST PUT DELETE /api_app/employee/
    Создание, обновление, удаление и просмотр  сотрудников в базе данных, в случае успеха   возвращяется код 201 в при некоректных данных код 400.

    GET /api_app/employee/$id_employee/
    Получение сотрудника по id.
---------------------------------------------------------------------------------------
### Установка
1. Загрузите исходный код проекта с помощью команды git clone:
```bash
git clone https://github.com/medikos/test_task_dom_click.git
```
2. Создайте виртуальное окружение и запустите его:
```bash
python3 -m venv env
source env/bin/activate



```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Перейдите в каталог test_task_dom_click/processing_applications/ и запустите миграции:
 ```bash
 python manage.py migrate
 ```
 5. Запустите тесты:
 ```bash
 pytest
 ```

