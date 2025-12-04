from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DashboardView,
    HuespedListView, HuespedCreateView, HuespedUpdateView, HuespedDeleteView,
    HabitacionListView, HabitacionCreateView, HabitacionUpdateView, HabitacionDeleteView,
    ReservaListView, ReservaCreateView, ReservaUpdateView, ReservaDeleteView,
    DetalleReservaListView, DetalleReservaCreateView, DetalleReservaUpdateView, DetalleReservaDeleteView,
    EmpleadoListView, EmpleadoCreateView, EmpleadoUpdateView, EmpleadoDeleteView,
    ServicioAdicionalListView, ServicioAdicionalCreateView, ServicioAdicionalUpdateView, ServicioAdicionalDeleteView,
    FacturaListView, FacturaCreateView, FacturaUpdateView, FacturaDeleteView,
    HuespedViewSet, HabitacionHotelViewSet, ReservaHotelViewSet, 
    DetalleReservaViewSet, EmpleadoHotelViewSet, ServicioAdicionalViewSet, 
    FacturaHotelViewSet
)

router = DefaultRouter()
router.register(r'huespedes', HuespedViewSet)
router.register(r'habitaciones', HabitacionHotelViewSet)
router.register(r'reservas', ReservaHotelViewSet)
router.register(r'detalles-reserva', DetalleReservaViewSet)
router.register(r'empleados', EmpleadoHotelViewSet)
router.register(r'servicios-adicionales', ServicioAdicionalViewSet)
router.register(r'facturas', FacturaHotelViewSet)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('api/', include(router.urls)),

    # Huesped URLs
    path('huespedes/', HuespedListView.as_view(), name='huesped_list'),
    path('huespedes/add/', HuespedCreateView.as_view(), name='huesped_add'),
    path('huespedes/<int:pk>/edit/', HuespedUpdateView.as_view(), name='huesped_edit'),
    path('huespedes/<int:pk>/delete/', HuespedDeleteView.as_view(), name='huesped_delete'),

    # Habitacion URLs
    path('habitaciones/', HabitacionListView.as_view(), name='habitacion_list'),
    path('habitaciones/add/', HabitacionCreateView.as_view(), name='habitacion_add'),
    path('habitaciones/<int:pk>/edit/', HabitacionUpdateView.as_view(), name='habitacion_edit'),
    path('habitaciones/<int:pk>/delete/', HabitacionDeleteView.as_view(), name='habitacion_delete'),

    # Reserva URLs
    path('reservas/', ReservaListView.as_view(), name='reserva_list'),
    path('reservas/add/', ReservaCreateView.as_view(), name='reserva_add'),
    path('reservas/<int:pk>/edit/', ReservaUpdateView.as_view(), name='reserva_edit'),
    path('reservas/<int:pk>/delete/', ReservaDeleteView.as_view(), name='reserva_delete'),

    # DetalleReserva URLs
    path('detalles-reserva/', DetalleReservaListView.as_view(), name='detalle_reserva_list'),
    path('detalles-reserva/add/', DetalleReservaCreateView.as_view(), name='detalle_reserva_add'),
    path('detalles-reserva/<int:pk>/edit/', DetalleReservaUpdateView.as_view(), name='detalle_reserva_edit'),
    path('detalles-reserva/<int:pk>/delete/', DetalleReservaDeleteView.as_view(), name='detalle_reserva_delete'),

    # Empleado URLs
    path('empleados/', EmpleadoListView.as_view(), name='empleado_list'),
    path('empleados/add/', EmpleadoCreateView.as_view(), name='empleado_add'),
    path('empleados/<int:pk>/edit/', EmpleadoUpdateView.as_view(), name='empleado_edit'),
    path('empleados/<int:pk>/delete/', EmpleadoDeleteView.as_view(), name='empleado_delete'),

    # ServicioAdicional URLs
    path('servicios-adicionales/', ServicioAdicionalListView.as_view(), name='servicio_adicional_list'),
    path('servicios-adicionales/add/', ServicioAdicionalCreateView.as_view(), name='servicio_adicional_add'),
    path('servicios-adicionales/<int:pk>/edit/', ServicioAdicionalUpdateView.as_view(), name='servicio_adicional_edit'),
    path('servicios-adicionales/<int:pk>/delete/', ServicioAdicionalDeleteView.as_view(), name='servicio_adicional_delete'),

    # Factura URLs
    path('facturas/', FacturaListView.as_view(), name='factura_list'),
    path('facturas/add/', FacturaCreateView.as_view(), name='factura_add'),
    path('facturas/<int:pk>/edit/', FacturaUpdateView.as_view(), name='factura_edit'),
    path('facturas/<int:pk>/delete/', FacturaDeleteView.as_view(), name='factura_delete'),
]
