from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
def inicializar(request):
    request.session["efectivo"] = 500000
    request.session["marketing"] = 10000
    request.session["IyD"] = 10000
    request.session["ampliacionplanta"] = 10000
    request.session["banco1"] = 100000
    request.session["banco2"] = 300000
    request.session["devolverbanco1"] = 0
    request.session["devolverbanco2"] = 0
    request.session["mes"] = 1
    request.session["personas"] = 2000
    request.session["produccion"] = 75
    request.session["precio"] = 39.99
    request.session["cantprodvendidos"] = 2000
    request.session["cantprodproducidos"] = 2000
    request.session["stock"] = 0
    request.session["mantenimiento"] = 1000
    request.session["sueldos"] = 3000
    request.session["impuestos"] = 3000
    request.session["costoprod"] = 1000
    request.session["alquieler"] = 2000
    request.session["suministros"] = 2000
    request.session["interesestotales"] = 0