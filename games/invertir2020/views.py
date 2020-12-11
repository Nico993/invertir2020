from django.shortcuts import render
from . import functions
from django import  forms

precio = [(19.99,19.99),(29.99,29.99),(39.99,39.99),(49.99,49.99)]
prod = [(25,"25%"),(50,"50%"),(75,"75%"),(100,"100%")] 

class decisionsform(forms.Form):
    prestamobanco1 = forms.FloatField(label="Prestamos Banco 1", required= True, min_value=0)
    prestamobanco2 = forms.FloatField(label="Prestamos Banco 2", required= True, min_value=0)
    Precio = forms.ChoiceField(choices= precio, label="Precio", required= True)
    Produccion = forms.ChoiceField(choices=prod, label="Produccion", required= True)
    marketing = forms.FloatField(label="Marketing", required= True, min_value=0)
    calidad = forms.FloatField(label="Calidad", required= True, min_value=0)
    maquinaria = forms.FloatField(label="Maquinaria", required= True, min_value=0)
    devolver1 = forms.FloatField(label="Devolver banco 1", required= True, min_value=0)
    devolver2 = forms.FloatField(label="Devolver banco 2", required= True, min_value=0)
# Create your views here.
def index(request):
    return render(request, "invertir2020/index.html")

def comojugar(request):
    return render(request, "invertir2020/comojugar.html")

def facil(request):
    functions.inicializar(request)
    request.session["dificultad"] = 1
    return render(request, "invertir2020/periodicoLayout.html",{
        "mes": request.session["mes"]
    })

def medio(request):
    functions.inicializar(request)
    request.session["dificultad"] = 2
    return render(request, "invertir2020/periodicoLayout.html",{
        "mes": request.session["mes"]

    })

def dificil(request):
    functions.inicializar(request)
    request.session["dificultad"] = 3
    return render(request, "invertir2020/periodicoLayout.html",{
        "mes": request.session["mes"]
    })

def resumen(request):
    return render(request, "invertir2020/resumenLayout.html",{
        "precio": round(request.session["precio"],2),
        "produccion": request.session["produccion"],
        "marketing": request.session["marketing"],
        "calidad": request.session["IyD"],
        "maquinaria": request.session["ampliacionplanta"],
        "cantprodproducidos": request.session["cantprodproducidos"],
        "cantperint": request.session["personas"],
        "cantprodvend": request.session["cantprodvendidos"],
        "stock": request.session["stock"],
        "mantenimiento": request.session["mantenimiento"],
        "sueldos": request.session["sueldos"],
        "impuestos": request.session["impuestos"],
        "costoprod": request.session["costoprod"],
        "alquiler": request.session["alquieler"],
        "suministros": request.session["suministros"],
        "intereses": request.session["interesestotales"],
        "efectivo": request.session["efectivo"],
        "banco1": request.session["banco1"],
        "banco2": request.session["banco2"],
        "devolver1": request.session["devolverbanco1"],
        "devolver2": request.session["devolverbanco2"]

    })
def decisiones(request):
    return render(request, "invertir2020/decisionesLayout.html",{
        "efectivo": request.session["efectivo"],
        "form": decisionsform()
    })
def periodico(request):
    if request.method == "POST":
        form = decisionsform(request.POST)
        if form.is_valid():
            prestamobanco1 = form.cleaned_data["prestamobanco1"]
            prestamobanco2 = form.cleaned_data["prestamobanco2"]
            Precio = form.cleaned_data["Precio"]
            Produccion = form.cleaned_data["Produccion"]
            marketing = form.cleaned_data["marketing"]
            calidad = form.cleaned_data["calidad"]
            maquinaria = form.cleaned_data["maquinaria"]
            devolver1 = form.cleaned_data["devolver1"]
            devolver2 = form.cleaned_data["devolver2"]
            request.session["mes"] = request.session["mes"] + 1
            band = functions.calculartodo(request, prestamobanco1, prestamobanco2, Precio, Produccion, marketing, calidad, maquinaria, devolver1, devolver2)
        else:
            return render(request, "invertir2020/decisionesLayout.html",{
                "form": form
            })
    if(request.session["mes"] == 13):
        return render(request, "invertir2020/ganaste.html")
    if band:
        return render(request, "invertir2020/periodicoLayout.html",{
            "mes": request.session["mes"]
        })
    else:
        return render(request, "invertir2020/perdiste.html")
