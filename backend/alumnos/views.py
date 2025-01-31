from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Alumno
from alumnos.serializers.serializer import CreateAlumnoSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class CreateAlumnoView(generics.CreateAPIView):
    queryset = Alumno.objects.all()
    serializer_class = CreateAlumnoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class GetAlumnosByGradeView(generics.ListAPIView):
    serializer_class = CreateAlumnoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        grado = self.kwargs['idGrado']
        if grado == 0:
            return Alumno.objects.all()
        return Alumno.objects.filter(grado=grado)
