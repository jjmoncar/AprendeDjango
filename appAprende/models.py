#encoding:utf-8

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

lista_tamano = (('Pequeño','Pequeño'), ('Mediano','Mediano'), ('Grande','Grande'),('Extra','Extra'))

class supermercados(models.Model):
	codsuper = models.CharField(max_length=12,unique=True,blank=False,primary_key=True)
	nombresuper = models.CharField(max_length=40,null=False)
	direccion = models.TextField(max_length=200,null=False)
	telefono = models.CharField(max_length=11,blank=True)
	email = models.EmailField(max_length=75,blank=False)
	estatus = models.BooleanField
	
	def __str__(self):
		return self.nombresuper

class departamentos(models.Model):
	coddpto = models.CharField(max_length=12,unique=True,blank=False,primary_key=True)
	nombredpto = models.CharField(max_length=80, blank=False,null=False)
	codsuper = models.ForeignKey('supermercados',on_delete=models.CASCADE,)
	
	def __str__(self):
		return self.nombredpto

class productos(models.Model):
	codproducto = models.CharField(max_length=12,unique=True,blank=False,primary_key=True)
	descripcion = models.TextField(max_length=200,null=False)
	marca = models.CharField(max_length=60,blank=False)
	foto = models.ImageField(upload_to='imagenes')
	tipo = models.CharField(max_length=60,blank=False)
	tamano = models.CharField(max_length=20,choices=lista_tamano)
	precio = models.DecimalField(max_digits=7,decimal_places=2)
	coddpto = models.ForeignKey('departamentos',on_delete=models.CASCADE,)
	
	def __str__(self):
		return self.codproducto

class ofertas(models.Model):
	codoferta = models.CharField(max_length=12,unique=True,blank=False,primary_key=True)
	descuento = models.DecimalField(max_digits=5,decimal_places=2)
	fecha_inicio =models.DateField(blank=False,null=False)
	fecha_fin = models.DateField(blank=False,null=False)
	condicion = models.BooleanField
	codproducto = models.ForeignKey('productos',on_delete=models.CASCADE,)
	
	def __str__(self):
		return self.codoferta
