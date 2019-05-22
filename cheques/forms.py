from django import forms
from django.forms.models import model_to_dict

#from others
#from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
import datetime

#from models
from cheques.models import (Distribuidor , Institucion_Bancaria , Chequera , CuentasBancarias,

    )


class DistribuidorForm(forms.ModelForm):

    class Meta:

        model = Distribuidor
        fields = (
        'nombre',
        )

class InstitucionForm(forms.ModelForm):

    class Meta:

        model = Institucion_Bancaria
        fields = (
        'institucion',
        )

class CuentasForm(forms.ModelForm):

    class Meta:

        model = CuentasBancarias
        fields = (
        'num',
        'banco',
        'titular'
        )


class ChequeForm(forms.ModelForm):

    class Meta:

        model = Chequera
        fields = (
        'No_Cheque',
        'total',
        'fecha_pago',
        'observacion',
        'imge_cheque',
        'distribuidor',
        'cuenta_bancaria'
        )
