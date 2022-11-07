from django.urls import path
from MiApp.views import  mostrar_familia


urlpatterns = [
    path('',mostrar_familia)
]