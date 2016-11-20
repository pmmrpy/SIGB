from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from geraldo.generators.pdf import PDFGenerator
from clientes.models import Reserva
from clientes.reports import ReservaReport
from .models import Cliente
from .forms import ClienteForm
# from dal import autocomplete

# Create your views here.


def reserva_report(request, pk):
    resp = HttpResponse(content_type='application/pdf')

    reserva = Reserva.objects.filter(id=pk)  # 107: ENTREGADA - 111: CANCELADA - 56: PENDIENTE
    report = ReservaReport(queryset=reserva)

    report.generate_by(PDFGenerator, filename=resp)

    return resp


# ======================================================================================================================
def index(request):
    clientes = Cliente.objects.all().order_by('-fecha_nacimiento')
    # return HttpResponse("Esta es la aplicacion de Clientes.")
    return render(request, 'clientes/index.html', {'clientes': clientes})


def cliente_detalle(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    return render(request, 'clientes/cliente_detalle.html', {'cliente': cliente})


def cliente_nuevo(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            # cliente.author = request.user
            # cliente.fecha_nacimiento = timezone.now()
            cliente.save()
            return redirect('cliente_detalle', cliente_id=cliente.pk)
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente_edit.html', {'form': form})


def cliente_edit(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente.save()
            return redirect('cliente_detalle', cliente_id=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/cliente_edit.html', {'form': form})


# class ClienteAutocomplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         # Don't forget to filter out results depending on the visitor !
#         if not self.request.user.is_authenticated():
#             return Cliente.objects.none()
#
#         qs = Cliente.objects.all()
#
#         if self.q:
#             # qs = qs.filter(name__istartswith=self.q)
#             qs = qs.filter(name__icontains=self.q)
#
#         return qs