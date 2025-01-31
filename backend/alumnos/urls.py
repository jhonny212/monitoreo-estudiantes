from django.urls import path
from alumnos.views import CreateAlumnoView, GetAlumnosByGradeView

urlpatterns = [
    path('crear-alumno', CreateAlumnoView.as_view(), name="crear_alumno"),
    path('consultar-alumno/<int:idGrado>', GetAlumnosByGradeView.as_view(), name="consultar_alumno"),
]
