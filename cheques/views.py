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
from cheques.models import Chequera , Distribuidor , Institucion_Bancaria

#from forms
from cheques.forms import DistribuidorForm , InstitucionForm


class IndexView(LoginRequiredMixin ,SuccessMessageMixin ,TemplateView ):
    template_name = 'cheques/index.html'

    def get_context_data(self , *args , **kwargs):
        cheques = Chequera.objects.all()
        return {'cheques' : cheques}

class CreateDistribuidor(LoginRequiredMixin, SuccessMessageMixin , CreateView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = 'cheques/form_distribuidor.html'
    form_class = DistribuidorForm
    success_url = reverse_lazy('index')
    success_message = 'El distribuidor se creo correctamente!'

    # def get_context_data(self, *args, **kwargs):
    #     clientes = Cliente.objects.all()
    #     return {"clientes": clientes}

class CreateAgenteB(LoginRequiredMixin, SuccessMessageMixin , CreateView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = 'cheques/form_instituciones.html'
    form_class = InstitucionForm
    success_url = reverse_lazy('index')
    success_message = 'la institucion bancaria se creo correctamente!'

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
