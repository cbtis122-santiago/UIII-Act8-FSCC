from django import forms
from .models import Huesped, HabitacionHotel, ReservaHotel, DetalleReserva, EmpleadoHotel, ServicioAdicional, FacturaHotel

class HuespedForm(forms.ModelForm):
    class Meta:
        model = Huesped
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/aaaa'}),
            'fecha_registro': forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/aaaa'}),
        }

class HabitacionHotelForm(forms.ModelForm):
    class Meta:
        model = HabitacionHotel
        fields = '__all__'
        widgets = {
            'tipo_habitacion': forms.Select(attrs={'class': 'form-control'}),
            'estado_habitacion': forms.Select(attrs={'class': 'form-control'}),
        }

class ReservaHotelForm(forms.ModelForm):
    class Meta:
        model = ReservaHotel
        fields = '__all__'
        widgets = {
            'fecha_entrada': forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/aaaa'}),
            'fecha_salida': forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/aaaa'}),
            'fecha_reserva': forms.DateTimeInput(attrs={'type': 'datetime-local', 'placeholder': 'dd/mm/aaaa hh:mm'}),
            'estado_reserva': forms.Select(attrs={'class': 'form-control'}),
        }

class DetalleReservaForm(forms.ModelForm):
    servicios_adicionales = forms.ModelMultipleChoiceField(
        queryset=ServicioAdicional.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = DetalleReserva
        fields = '__all__'

class EmpleadoHotelForm(forms.ModelForm):
    class Meta:
        model = EmpleadoHotel
        fields = '__all__'
        widgets = {
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/aaaa'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
        }

class ServicioAdicionalForm(forms.ModelForm):
    class Meta:
        model = ServicioAdicional
        fields = '__all__'
        widgets = {
            'disponible': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'duracion': forms.Select(attrs={'class': 'form-control'}),
        }

class FacturaHotelForm(forms.ModelForm):
    class Meta:
        model = FacturaHotel
        fields = '__all__'
        widgets = {
            'fecha_emision': forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/aaaa'}),
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/aaaa'}),
            'estado_pago': forms.Select(attrs={'class': 'form-control'}),
            'metodo_pago': forms.Select(attrs={'class': 'form-control'}),
        }
