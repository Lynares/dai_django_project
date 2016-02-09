# -*- encoding: utf-8 -*-
from django.shortcuts import render
# Importamos Bares
from bares.models import Bares, Tapas
# Importamos del script forms para crear Tapas.
from bares.forms import TapasForm, RegisterForm
# Importamos para login:
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
# Para la restriccion de acceso
from django.contrib.auth.decorators import login_required
# Para JSon
from django.http import JsonResponse

def index(request):
    bar_list = Bares.objects.order_by('n_bar')[:10] #orden ascendente a-z, orden descendente z-a con ('-nombre')
    tapas_list = Tapas.objects.order_by('-votos')[:10] # lo visualizamos de más votos a menos
    context_dict = {'bares': bar_list, 'tapas': tapas_list}

    return render(request, 'bares/index.html', context_dict)

def bar(request, bar_nombre_slug):

    context_dict = {}

    try:
        bar = Bares.objects.get(slug=bar_nombre_slug)
        context_dict['bar_nombre'] = bar.n_bar
        context_dict['bar_direccion'] = bar.direccion
        #Para aumentar el numero de visitas con cada peticion de la pagina de un bar, incrementamos, pasamos a context_dict y guardamos
        bar.visitas = bar.visitas+1
        context_dict['bar_visitas'] = bar.visitas
        bar.save()

        tapas = Tapas.objects.filter(n_bar=bar)


        context_dict['tapas'] = tapas
        context_dict['bar'] = bar
    except Bares.DoesNotExist:
        pass

    return render(request, 'bares/bar.html', context_dict)

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = RegisterForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print user_form.errors

    else:
        user_form = RegisterForm()

    return render(request,'bares/register.html',
            {'user_form': user_form, 'registered': registered} )

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/bares/')
            else:
                return HttpResponse("Tu cuenta en Bares ha sido deshabilitada.")
        else:
            print "Login invalido : {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'bares/login.html', {})

@login_required
def restricted(request): 
    return HttpResponse('Si estas logeado podras ver este mensaje')


@login_required
def user_logout(request): 
    logout(request)

    return HttpResponseRedirect('/bares/')

@login_required
def add_tapas(request, bar_nombre_slug): 

    try: 
        bares = Bares.objects.get(slug=bar_nombre_slug)
    except Bares.DoesNotExist: 
        bares = None

    if request.method == 'POST': 
        form = TapasForm(request.POST)
        if form.is_valid(): 
            if bares:
                tapa = form.save(commit=False)
                tapa.n_bar = bares
                tapa.votos = 1
                tapa.save()

                return HttpResponseRedirect('/bares/')
     
        else:
            print form.errors

    else:
        form = TapasForm()

    context_dict = {'form':form, 'bares':bares}

    return render(request, 'bares/add_tapas.html', context_dict)

def reclama_datos(request): 
    # Como en el populated solo creamos tres bares, mostramos 3, pero si alguno que se cree mediante admin acaba superando a otro en visitas se mostrara este
    bares_list = Bares.objects.order_by('-visitas')[:3]

    datos = {
        'lista_bares':[bares_list[0].n_bar, bares_list[1].n_bar, bares_list[2].n_bar],
        'visit':[bares_list[0].visitas, bares_list[1].visitas, bares_list[2].visitas]
    } 
    return JsonResponse(datos, safe=False)