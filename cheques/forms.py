from django import forms
from django.forms.models import model_to_dict

#from others
#from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
import datetime

#from models
from cheques.models import Distribuidor , Institucion_Bancaria , Chequera


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
