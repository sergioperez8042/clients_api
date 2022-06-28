from django.urls import path
from .views import ClientView

urlpatterns =[
    path('clients/',ClientView.as_view(), name= 'clients'),
    path('clients/<int:id>',ClientView.as_view(), name= 'clients_process'),

]
