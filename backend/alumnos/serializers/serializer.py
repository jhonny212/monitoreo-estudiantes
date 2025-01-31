from rest_framework import serializers
from alumnos.models import Alumno

class CreateAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'
