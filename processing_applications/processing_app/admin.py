from django.contrib import admin
from processing_app.models import Application, StatusApplication, Client,Position,Employee,TypeApplication



@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
     list_display = ('id', 'date_created', 'status','type','client','employee','description')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(StatusApplication)
class StatusApplicationAdmin(admin.ModelAdmin):
    pass

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

@admin.register(TypeApplication)
class TypeApplication(admin.ModelAdmin):
    pass
    