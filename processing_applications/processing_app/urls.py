

from django.urls import path
from processing_app.views import (application_view, client_view, client_detail_view, 
                                    application_detail_view, employee_detail_view,employee_view)




urlpatterns = [
        
    path('application/', application_view),
    path('application/<int:pk>/', application_detail_view),
    path('client/',client_view),
    path('client/<int:pk>/', client_detail_view,),
    path('employee/', employee_view),
    path('employee/<int:pk>', employee_detail_view)
    

]