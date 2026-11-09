import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import categoria, productos, clientes, venta, Detalleventa
from .forms import CategoriaForm, ProductoForm, ClienteForm


def index(request):
    return render(request, 'tienda/index.html')

def lista_categorias(request):
    q = request.GET.get('q', '').strip()
    lista = categoria.objects.all()

    if q:
        lista = lista.filter(nombre__icontains=q)

    return render(request, 'tienda/lista_categorias.html', {
        'lista': lista,
        'q': q
    })


def crear_categoria(request):
    form = CategoriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_categorias')

    return render(request, 'tienda/form.html', {
        'form': form,
        'titulo': 'Nueva categoría'
    })


def editar_categoria(request, pk):
    obj = get_object_or_404(categoria, pk=pk)
    form = CategoriaForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('lista_categorias')

    return render(request, 'tienda/form.html', {
        'form': form,
        'titulo': 'Editar categoría'
    })


def eliminar_categoria(request, pk):
    obj = get_object_or_404(categoria, pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('lista_categorias')

    return render(request, 'tienda/confirmar_eliminar.html', {
        'obj': obj,
        'volver': 'lista_categorias'
    })

def lista_productos(request):
    q = request.GET.get('q', '').strip()
    lista = productos.objects.select_related('categoria').all()

    if q:
        lista = lista.filter(
            Q(nombre__icontains=q) |
            Q(categoria__nombre__icontains=q)
        )

    return render(request, 'tienda/lista_productos.html', {
        'lista': lista,
        'q': q
    })


def crear_producto(request):
    form = ProductoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_productos')

    return render(request, 'tienda/form.html', {
        'form': form,
        'titulo': 'Nuevo producto'
    })


def editar_producto(request, pk):
    obj = get_object_or_404(productos, pk=pk)
    form = ProductoForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('lista_productos')

    return render(request, 'tienda/form.html', {
        'form': form,
        'titulo': 'Editar producto'
    })


def eliminar_producto(request, pk):
    obj = get_object_or_404(productos, pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('lista_productos')

    return render(request, 'tienda/confirmar_eliminar.html', {
        'obj': obj,
        'volver': 'lista_productos'
    })

def lista_clientes(request):
    q = request.GET.get('q', '').strip()
    lista = clientes.objects.all()

    if q:
        lista = lista.filter(nombre__icontains=q)

    return render(request, 'tienda/lista_clientes.html', {
        'lista': lista,
        'q': q
    })


def crear_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_clientes')

    return render(request, 'tienda/form.html', {
        'form': form,
        'titulo': 'Nuevo cliente'
    })


def editar_cliente(request, pk):
    obj = get_object_or_404(clientes, pk=pk)
    form = ClienteForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('lista_clientes')

    return render(request, 'tienda/form.html', {
        'form': form,
        'titulo': 'Editar cliente'
    })


def eliminar_cliente(request, pk):
    obj = get_object_or_404(clientes, pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('lista_clientes')

    return render(request, 'tienda/confirmar_eliminar.html', {
        'obj': obj,
        'volver': 'lista_clientes'
    })

def lista_venta(request):
    lista = venta.objects.select_related('cliente').all()

    return render(request, 'tienda/lista_venta.html', {
        'lista': lista
    })


def lista_detalle_ventas(request):
    lista = Detalleventa.objects.select_related(
        'venta', 'producto', 'venta__cliente'
    ).all()

    return render(request, 'tienda/lista_detalle_ventas.html', {
        'lista': lista
    })

def api_motos(request):

    url = "https://vpic.nhtsa.dot.gov/api/vehicles/GetMakesForVehicleType/Motorcycle"

    try:
        respuesta = requests.get(
            url,
            params={'format': 'json'},
            timeout=15
        )

        respuesta.raise_for_status()

        datos = respuesta.json()
        motos = datos.get('Results', [])

        error = None

    except requests.RequestException:
        motos = []
        error = 'No se pudo conectar con la API. Intenta nuevamente.'

    return render(request, 'tienda/api_motos.html', {
        'motos': motos,
        'error': error
    })
