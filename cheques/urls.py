
from django.urls import path
from cheques.views import (IndexView , CreateDistribuidor , DistribuidorList , CreateAgenteB,
InstitucionesList , CreateCheque , CreateCuentas , ChequesList , CuentasList , UpdateDistribuidor,
UpdateBancos, UpdateCheques , search_cheque_fecha , ChequeDetailView , search_cheque_banco ,
search_cheque_cuenta, LoginView , LogoutView
    )

urlpatterns = [
    path('' , IndexView.as_view() , name='index'),
    path('agregar/distribuidor/' , CreateDistribuidor.as_view() , name='crear_distribuidor'),
    path('ver/distribuidor/' , DistribuidorList.as_view() , name='distribuidor_client'),
    path('agregar/institucion/' , CreateAgenteB.as_view() , name='crear_institucion'),
    path('ver/institucion/' , InstitucionesList.as_view() , name='ver_institucion'),
    path('agregar/cheque/' , CreateCheque.as_view() , name='crear_cheque'),
    path('agregar/cuenta/' , CreateCuentas.as_view() , name='crear_cuenta'),
    # path('ver/cheques/' , ChequesList.as_view() , name='ver_cheques'),
    path('ver/cuentas/' , CuentasList.as_view() , name='ver_cuentas'),
    path('actualizar/distribuidor/<int:pk>' , UpdateDistribuidor.as_view() , name='update_distribuidor'),
    path('actualizar/banco/<int:pk>' , UpdateBancos.as_view() , name='update_bancos'),
    path('actualizar/cheque/<int:pk>' , UpdateCheques.as_view() , name='update_cheque'),
    path('detalle/cheque/<int:id_chequera>' , ChequeDetailView.as_view() , name='detail_cheque'),
    path('buscar/cheque/fecha' , search_cheque_fecha , name='search_cheque'),
    path('buscar/cheque/banco' , search_cheque_banco , name='search_cheque_banco'),
    path('buscar/cheque/cuenta' , search_cheque_cuenta , name='search_cheque_cuenta'),
    path('login/' , LoginView.as_view() , name='login'),
    path('logout' , LogoutView.as_view() , name='logout'),

]
