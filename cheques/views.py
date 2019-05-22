from django.shortcuts import render , get_object_or_404 , render_to_response
from django.views.generic import FormView , CreateView , TemplateView , DetailView , DeleteView , UpdateView , ListView
from django.urls import reverse , reverse_lazy
from django.db.models import Q  , Sum , Avg , Count
from django.http import HttpResponseRedirect , JsonResponse, HttpResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#from models
from cheques.models import Chequera , Distribuidor , Institucion_Bancaria , CuentasBancarias

#from forms
from cheques.forms import DistribuidorForm , InstitucionForm , ChequeForm , CuentasForm


class IndexView(LoginRequiredMixin ,SuccessMessageMixin ,TemplateView ):
    template_name = 'cheques/index.html'

    def get_context_data(self , *args , **kwargs):
        cheques = Chequera.objects.all()
        return {'cheques' : cheques}

''' TODAS LAS CREATES VIEWS '''

class CreateCuentas(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = 'cheques/form_cuentas.html'
    form_class = CuentasForm
    success_url = reverse_lazy('index')
    success_message = 'la  cuenta bancaria se agrego correctamente!'

    def get_context_data(self, *args, **kwargs):
        instituciones = Institucion_Bancaria.objects.all()
        return {"instituciones": instituciones}

class CreateCheque(LoginRequiredMixin, SuccessMessageMixin , CreateView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = 'cheques/form_cheques.html'
    form_class = ChequeForm
    success_url = reverse_lazy('index')
    success_message = 'El cheque se guardo correctamente!'

    def get_context_data(self, *args, **kwargs):
        instituciones = Institucion_Bancaria.objects.all()
        distribuidores = Distribuidor.objects.all()
        cuentas = CuentasBancarias.objects.all().order_by('banco')
        return {"instituciones": instituciones , "distribuidores": distribuidores , "cuentas" : cuentas}

class CreateDistribuidor(LoginRequiredMixin, SuccessMessageMixin , CreateView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = 'cheques/form_distribuidor.html'
    form_class = DistribuidorForm
    success_url = reverse_lazy('index')
    success_message = 'El distribuidor se creo correctamente!'

class CreateAgenteB(LoginRequiredMixin, SuccessMessageMixin , CreateView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = 'cheques/form_instituciones.html'
    form_class = InstitucionForm
    success_url = reverse_lazy('index')
    success_message = 'Felicidades, El banco se agrego correctamente!. -Consulta tus bancos asociados en : -"Bancos > Ver Bancos" '


''' AREA DE VISTAS DE LISTA '''

class DistribuidorList(LoginRequiredMixin ,ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'cheques/distribuidor_list.html'
    model = Distribuidor
    paginate_by = 10
    queryset = distribuidor = Distribuidor.objects.all().order_by("-nombre")

class InstitucionesList(LoginRequiredMixin ,ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'cheques/agencias_list.html'
    model = Institucion_Bancaria
    paginate_by = 10
    queryset = institucion = Institucion_Bancaria.objects.all().order_by("-institucion")

class ChequesList(LoginRequiredMixin ,ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'cheques/cheques_list.html'
    model = Chequera
    paginate_by = 10
    queryset = chequera = Chequera.objects.all().order_by("-fecha_creado")

class CuentasList(LoginRequiredMixin ,ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'cheques/cuentas_list.html'
    model = CuentasBancarias
    paginate_by = 10
    queryset = cuenta = CuentasBancarias.objects.all().order_by("banco")


'''AREA DE MODIFICACIONES '''


'''AREA DE ELIMINACIONES '''

'''AREA DE DETALLES'''
