from django.db import models
from django.contrib.auth import get_user_model

AuthUser = get_user_model()

class Institucion_Bancaria(models.Model):
    id_institucion = models.AutoField(primary_key=True)
    institucion = models.CharField('Bancos', max_length=100 , blank=False, unique=True)

    def __str__(self):
        return "%s" % (self.institucion)


class Distribuidor(models.Model):
    id_distribuidor = models.AutoField(primary_key=True)
    nombre = models.CharField('Distribuidores', max_length=200, blank=False, unique=True)

    def __str__(self):
        return "%s" % (self.nombre)

class CuentasBancarias(models.Model):
    id_cuenta = models.AutoField(primary_key=True)
    banco = models.ForeignKey(Institucion_Bancaria , on_delete=models.CASCADE)
    num = models.CharField('No. Cuenta' , max_length=20 , unique=True)
    titular = models.CharField('Titular' , max_length=100)

    def __str__(self):
        return "%s %s %s" % (self.num , self.banco, self.titular )

class Chequera(models.Model):
    id_chequera = models.AutoField(primary_key=True)
    No_Cheque = models.CharField('Cheque No.', max_length=10)
    total = models.CharField('Total', max_length=15 )
    fecha_creado = models.DateField('Fecha de elaboracion' , auto_now_add=True)
    fecha_pago = models.DateField('Fecha a Pagar' , blank=True )
    observacion = models.TextField('Observaciones' , blank=True)
    imge_cheque = models.ImageField(upload_to='cheques/pictures')
    # institucion_bancaria = models.ForeignKey(Institucion_Bancaria , on_delete=models.CASCADE)
    distribuidor = models.ForeignKey(Distribuidor , on_delete=models.CASCADE)
    cuenta_bancaria = models.ForeignKey(CuentasBancarias , on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.No_Cheque  ,self.total, self.cuenta_bancaria)
