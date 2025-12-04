from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from rest_framework import viewsets
from .models import (
    Huesped, HabitacionHotel, ReservaHotel, DetalleReserva,
    EmpleadoHotel, ServicioAdicional, FacturaHotel
)
from .serializers import (
    HuespedSerializer, HabitacionHotelSerializer, ReservaHotelSerializer,
    DetalleReservaSerializer, EmpleadoHotelSerializer,
    ServicioAdicionalSerializer, FacturaHotelSerializer
)
from .forms import (
    HuespedForm, HabitacionHotelForm, ReservaHotelForm,
    DetalleReservaForm, EmpleadoHotelForm, ServicioAdicionalForm,
    FacturaHotelForm
)

# --- Dashboard View ---
class DashboardView(TemplateView):
    template_name = 'hotel/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_huespedes'] = Huesped.objects.count()
        context['total_habitaciones'] = HabitacionHotel.objects.count()
        context['total_reservas'] = ReservaHotel.objects.count()
        context['habitaciones_disponibles'] = HabitacionHotel.objects.filter(estado_habitacion='disponible').count()
        return context

# --- Huesped Views ---
class HuespedListView(ListView):
    model = Huesped
    template_name = 'hotel/huesped_list.html'
    context_object_name = 'huespedes'

class HuespedCreateView(CreateView):
    model = Huesped
    form_class = HuespedForm
    template_name = 'hotel/huesped_form.html'
    success_url = reverse_lazy('huesped_list')

class HuespedUpdateView(UpdateView):
    model = Huesped
    form_class = HuespedForm
    template_name = 'hotel/huesped_form.html'
    success_url = reverse_lazy('huesped_list')

class HuespedDeleteView(DeleteView):
    model = Huesped
    template_name = 'hotel/confirm_delete.html'
    success_url = reverse_lazy('huesped_list')

# --- Habitacion Views ---
class HabitacionListView(ListView):
    model = HabitacionHotel
    template_name = 'hotel/habitacion_list.html'
    context_object_name = 'habitaciones'

class HabitacionCreateView(CreateView):
    model = HabitacionHotel
    form_class = HabitacionHotelForm
    template_name = 'hotel/habitacion_form.html'
    success_url = reverse_lazy('habitacion_list')

class HabitacionUpdateView(UpdateView):
    model = HabitacionHotel
    form_class = HabitacionHotelForm
    template_name = 'hotel/habitacion_form.html'
    success_url = reverse_lazy('habitacion_list')

class HabitacionDeleteView(DeleteView):
    model = HabitacionHotel
    template_name = 'hotel/confirm_delete.html'
    success_url = reverse_lazy('habitacion_list')

# --- Reserva Views ---
class ReservaListView(ListView):
    model = ReservaHotel
    template_name = 'hotel/reserva_list.html'
    context_object_name = 'reservas'

class ReservaCreateView(CreateView):
    model = ReservaHotel
    form_class = ReservaHotelForm
    template_name = 'hotel/reserva_form.html'
    success_url = reverse_lazy('reserva_list')

class ReservaUpdateView(UpdateView):
    model = ReservaHotel
    form_class = ReservaHotelForm
    template_name = 'hotel/reserva_form.html'
    success_url = reverse_lazy('reserva_list')

class ReservaDeleteView(DeleteView):
    model = ReservaHotel
    template_name = 'hotel/confirm_delete.html'
    success_url = reverse_lazy('reserva_list')

# --- DetalleReserva Views ---
class DetalleReservaListView(ListView):
    model = DetalleReserva
    template_name = 'hotel/detalle_reserva_list.html'
    context_object_name = 'detalles'

class DetalleReservaCreateView(CreateView):
    model = DetalleReserva
    form_class = DetalleReservaForm
    template_name = 'hotel/detalle_reserva_form.html'
    success_url = reverse_lazy('detalle_reserva_list')

class DetalleReservaUpdateView(UpdateView):
    model = DetalleReserva
    form_class = DetalleReservaForm
    template_name = 'hotel/detalle_reserva_form.html'
    success_url = reverse_lazy('detalle_reserva_list')

class DetalleReservaDeleteView(DeleteView):
    model = DetalleReserva
    template_name = 'hotel/confirm_delete.html'
    success_url = reverse_lazy('detalle_reserva_list')

# --- Empleado Views ---
class EmpleadoListView(ListView):
    model = EmpleadoHotel
    template_name = 'hotel/empleado_list.html'
    context_object_name = 'empleados'

class EmpleadoCreateView(CreateView):
    model = EmpleadoHotel
    form_class = EmpleadoHotelForm
    template_name = 'hotel/empleado_form.html'
    success_url = reverse_lazy('empleado_list')

class EmpleadoUpdateView(UpdateView):
    model = EmpleadoHotel
    form_class = EmpleadoHotelForm
    template_name = 'hotel/empleado_form.html'
    success_url = reverse_lazy('empleado_list')

class EmpleadoDeleteView(DeleteView):
    model = EmpleadoHotel
    template_name = 'hotel/confirm_delete.html'
    success_url = reverse_lazy('empleado_list')

# --- ServicioAdicional Views ---
class ServicioAdicionalListView(ListView):
    model = ServicioAdicional
    template_name = 'hotel/servicio_adicional_list.html'
    context_object_name = 'servicios'

class ServicioAdicionalCreateView(CreateView):
    model = ServicioAdicional
    form_class = ServicioAdicionalForm
    template_name = 'hotel/servicio_adicional_form.html'
    success_url = reverse_lazy('servicio_adicional_list')

class ServicioAdicionalUpdateView(UpdateView):
    model = ServicioAdicional
    form_class = ServicioAdicionalForm
    template_name = 'hotel/servicio_adicional_form.html'
    success_url = reverse_lazy('servicio_adicional_list')

class ServicioAdicionalDeleteView(DeleteView):
    model = ServicioAdicional
    template_name = 'hotel/confirm_delete.html'
    success_url = reverse_lazy('servicio_adicional_list')

# --- Factura Views ---
class FacturaListView(ListView):
    model = FacturaHotel
    template_name = 'hotel/factura_list.html'
    context_object_name = 'facturas'

class FacturaCreateView(CreateView):
    model = FacturaHotel
    form_class = FacturaHotelForm
    template_name = 'hotel/factura_form.html'
    success_url = reverse_lazy('factura_list')

class FacturaUpdateView(UpdateView):
    model = FacturaHotel
    form_class = FacturaHotelForm
    template_name = 'hotel/factura_form.html'
    success_url = reverse_lazy('factura_list')

class FacturaDeleteView(DeleteView):
    model = FacturaHotel
    template_name = 'hotel/confirm_delete.html'
    success_url = reverse_lazy('factura_list')


# --- API ViewSets (Not part of the main UI flow but good to have) ---
class HuespedViewSet(viewsets.ModelViewSet):
    queryset = Huesped.objects.all()
    serializer_class = HuespedSerializer

class HabitacionHotelViewSet(viewsets.ModelViewSet):
    queryset = HabitacionHotel.objects.all()
    serializer_class = HabitacionHotelSerializer

class ReservaHotelViewSet(viewsets.ModelViewSet):
    queryset = ReservaHotel.objects.all()
    serializer_class = ReservaHotelSerializer

class DetalleReservaViewSet(viewsets.ModelViewSet):
    queryset = DetalleReserva.objects.all()
    serializer_class = DetalleReservaSerializer

class EmpleadoHotelViewSet(viewsets.ModelViewSet):
    queryset = EmpleadoHotel.objects.all()
    serializer_class = EmpleadoHotelSerializer

class ServicioAdicionalViewSet(viewsets.ModelViewSet):
    queryset = ServicioAdicional.objects.all()
    serializer_class = ServicioAdicionalSerializer

class FacturaHotelViewSet(viewsets.ModelViewSet):
    queryset = FacturaHotel.objects.all()
    serializer_class = FacturaHotelSerializer
