from rest_framework import serializers
from .models import Huesped, HabitacionHotel, ReservaHotel, DetalleReserva, EmpleadoHotel, ServicioAdicional, FacturaHotel

class HuespedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Huesped
        fields = '__all__'

class HabitacionHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitacionHotel
        fields = '__all__'

class ReservaHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaHotel
        fields = '__all__'

class DetalleReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleReserva
        fields = '__all__'

class EmpleadoHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpleadoHotel
        fields = '__all__'

class ServicioAdicionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioAdicional
        fields = '__all__'

class FacturaHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaHotel
        fields = '__all__'
