from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name = "index"),
    path("facil", views.facil, name = "facil"),
    path("medio", views.medio, name="medio"),
    path("dificil",views.dificil, name = "dificil"),
    path("ComoJugar", views.comojugar, name = "comojugar"),
    path("resumen",views.resumen, name = "res"),
    path("decisiones",views.decisiones, name = "decisiones"),
    path("periodico", views.periodico, name="periodico")
]