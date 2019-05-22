from django.db import models

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

class Chequera(models.Model):
    No_Cheque = models.CharField('Cheque No.', max_length=10)
    total = models.CharField('Total', max_length=15 )
    fecha_creado = models.DateField('Fecha de elaboracion')
    fecha_pago = models.DateField('Fecha a Pagar')
    observacion = models.TextField('Observaciones' , blank=True)
    imge_cheque = models.ImageField(upload_to='cheque/pictures')
    institucion_bancaria = models.ForeignKey(Institucion_Bancaria , on_delete=models.CASCADE)
    distribuidor = models.ForeignKey(Distribuidor , on_delete=models.CASCADE)
    cuenta_bancaria = models.CharField('Cuenta Bancaria', max_length=30)

    def __str__(self):
        return "%s %s %s" % (self.No_Cheque  ,self.total, self.cuenta_bancaria)
