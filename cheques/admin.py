from django.contrib import admin
from cheques.models import Institucion_Bancaria , Distribuidor , Chequera , CuentasBancarias

# Register your models here.
class ChequesAdmin(admin.ModelAdmin):
    #raw_id_fields = ( "No_Cheque",)
    search_fields = ['No_Cheque' , 'fecha_creado']
    list_display = ['No_Cheque' , 'total' , 'fecha_creado' ]

class DistribuidorAdmin(admin.ModelAdmin):
    #raw_id_fields = ( "No_Cheque",)
    search_fields = ['id_distribuidor' , 'nombre']
    list_display = ['id_distribuidor' , 'nombre']

class InstitucionAdmin(admin.ModelAdmin):
    #raw_id_fields = ( "No_Cheque",)
    search_fields = ['id_institucion' , 'institucion']
    list_display = ['id_institucion' , 'institucion']

class CuentasBancariasAdmin(admin.ModelAdmin):
    list_display = ['num' , 'banco' ,'titular']

admin.site.register(Chequera , ChequesAdmin)
admin.site.register(Distribuidor, DistribuidorAdmin)
admin.site.register(Institucion_Bancaria , InstitucionAdmin)
admin.site.register(CuentasBancarias , CuentasBancariasAdmin)
