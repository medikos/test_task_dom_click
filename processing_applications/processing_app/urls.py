

from django.urls import path
from processing_app.views import index




urlpatterns = [
        
    path('', index)
    

]