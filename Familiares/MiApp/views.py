from django.shortcuts import render

# Create your views here.
from MiApp.models import Familiares

def mostrar_familia(request):

    fam1 = Familiares(nombre='Moisés', apellido= 'Espinosa', telefono = 123456789, cumple ='1980-05-11')
    fam2 = Familiares(nombre='Matilde', apellido= 'Mendoza', telefono = 127536789, cumple ='1986-10-30')
    fam3 = Familiares(nombre='Julian', apellido= 'Paredes', telefono = 123451599, cumple ='1998-02-23')

    return render(request,'MiApp/familiares.html', {'familiares':[fam1,fam2,fam3]})