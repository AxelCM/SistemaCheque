# Generated by Django 2.2.1 on 2019-05-22 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cheques', '0004_remove_chequera_institucion_bancaria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chequera',
            name='cuenta_bancaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cheques.CuentasBancarias'),
        ),
    ]
