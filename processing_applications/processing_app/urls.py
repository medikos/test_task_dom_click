

from django.urls import path
from processing_app.views import index, client_view




urlpatterns = [
        
    path('', index),
    path('client/',client_view),
    

]