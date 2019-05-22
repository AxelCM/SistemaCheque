from django import urls
from django.urls import path
from cheques.views import (IndexView , CreateDistribuidor , DistribuidorList , CreateAgenteB,
InstitucionesList
    )

urlpatterns = [
    path('' , IndexView.as_view() , name='index'),
    path('agregar/distribuidor/' , CreateDistribuidor.as_view() , name='crear_distribuidor'),
    path('ver/distribuidor/' , DistribuidorList.as_view() , name='distribuidor_client'),
    path('agregar/institucion/' , CreateAgenteB.as_view() , name='crear_institucion'),
    path('ver/institucion/' , InstitucionesList.as_view() , name='ver_institucion'),

]
