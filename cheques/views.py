from django.shortcuts import render , get_object_or_404 , render_to_response
from django.views.generic import FormView , CreateView , TemplateView , DetailView , DeleteView , UpdateView , ListView
from django.urls import reverse , reverse_lazy
from django.db.models import Q  , Sum , Avg , Count
from django.http import HttpResponseRedirect , JsonResponse, HttpResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

#from models
from cheques.models import Chequera , Distribuidor , Institucion_Bancaria , CuentasBancarias

#from forms
from cheques.forms import DistribuidorForm , InstitucionForm , ChequeForm , CuentasForm


class IndexView(LoginRequiredMixin ,SuccessMessageMixin ,TemplateView ):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
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
    success_url = reverse_lazy('distribuidor_client')
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
class UpdateDistribuidor(LoginRequiredMixin ,SuccessMessageMixin , UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Distribuidor
    fields = ['nombre'
        ]
    success_url = reverse_lazy('distribuidor_client')
    success_message = "los campos se actualizaron con exito"
    error_message = "Algo salio mal, no se ejecuto correctamente"
    template_name = 'cheques/update_form_distribuidor.html'


class UpdateBancos(LoginRequiredMixin ,SuccessMessageMixin , UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Institucion_Bancaria
    fields = ['institucion'
        ]
    success_url = reverse_lazy('ver_institucion')
    success_message = "los campos se actualizaron con exito"
    error_message = "Algo salio mal, no se ejecuto correctamente"
    template_name = 'cheques/update_form_bancos.html'

class UpdateCheques(LoginRequiredMixin ,SuccessMessageMixin , UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Chequera
    fields = ['No_Cheque',
            'total',
            'fecha_pago',
            'observacion',
            'imge_cheque',
            'distribuidor',
            'cuenta_bancaria'
        ]
    success_url = reverse_lazy('index')
    success_message = "los campos se actualizaron con exito"
    error_message = "Algo salio mal, no se ejecuto correctamente"
    template_name = 'cheques/update_form_cheques.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_chequera = self.get_object()
        context['cuentas'] = CuentasBancarias.objects.all()
        context['distribuidores'] = Distribuidor.objects.all()
        return context

'''AREA DE ELIMINACIONES '''

'''AREA DE DETALLES'''
class ChequeDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'cheques/detail_cheque.html'
    slug_field = 'id_chequera'
    slug_url_kwarg = 'id_chequera'
    queryset = Chequera.objects.all()
    context_object_name = 'cheque'

    # def get_context_data(self, **kwargs):
    #     """Add user's posts to context."""
    #     context = super().get_context_data(**kwargs)
    #     id_pedidos = self.get_object()
    #     context['cuentas'] = CuentasBancarias.objects.filter(banco__institucion=)
    #     context['distriubidores'] = ItemPedido.objects.filter(id_pedido=id_pedidos)
    #     return context






'''Busqueda'''
@login_required
def search_cheque_fecha(request):
    query = request.GET.get('q' , '')
    query2 = query.split('-')
    q = request.GET.get('q' , '')
    if query:
        qset = (
            Q(fecha_pago__icontains=query)
            )
        results = Chequera.objects.filter(qset).order_by('-fecha_pago')
    else:
        results = []
    return render(request  ,"cheques/search_cheque.html", {"results": results ,"query": query , })

@login_required
def search_cheque_banco(request):
    bancos = Institucion_Bancaria.objects.all().order_by('institucion')
    query = request.GET.get('q' , '')
    if query:
        qset = (
            Q(cuenta_bancaria__banco__institucion__icontains=query)
            )
        results = Chequera.objects.filter(qset).order_by('-fecha_pago')

    else:
        results = []
    return render(request  ,"cheques/search_cheque_banco.html", {"results": results ,"query": query , "bancos" : bancos })

@login_required
def search_cheque_cuenta(request):
    cuentas = CuentasBancarias.objects.all().order_by('titular')
    query = request.GET.get('q' , '')
    q = request.GET.get('q' , '')
    if query:
        qset = (
            Q(cuenta_bancaria__num__icontains=query)
            )
        results = Chequera.objects.filter(qset).order_by('-fecha_pago')
    else:
        results = []
    return render(request  ,"cheques/search_cheque_cuentas.html", {"results": results ,"query": query , "cuentas" : cuentas })

class LoginView(SuccessMessageMixin , auth_views.LoginView):
    template_name = 'cheques/login.html'
    success_message = "Bienvenido!"


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    pass
