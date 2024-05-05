from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio , name="inicio"),
    path("ver_cursos", views.ver_cursos , name="cursos"),
    path("ver_alumnos", views.ver_alumnos , name="alumnos"),
    path("ver_profesores", views.ver_profesores , name="profesores"),
    # path("alta_alumno/<nombre>", views.alta_alumno),
    # path("alta_profesor/<nombre>", views.alta_profesor),
    # path("alta_curso/<nombre>", views.alta_curso),
    path("alta_alumno", views.alumno_formulario, name="falumno"),
    path("alta_profesor", views.profesor_formulario, name="fprofesor"),
    path("alta_curso", views.curso_formulario, name="fcurso"),
    path("comentarios", views.comentarios , name="comentario"),
    path("buscar_curso", views.buscar_curso, name="bcursos"),
    path("buscar_alumno", views.buscar_alumno, name="balumnos"),
    path("buscar_profesor", views.buscar_profesor, name="bprofesores"),
    path("busquedas", views.busquedas, name="busquedas"),
    path("buscar", views.buscar),
    path("elimina_curso/<int:id>", views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    path("elimina_profesor/<int:id>", views.elimina_profesor , name="elimina_profesor"),
    path("editar_profesor/<int:id>" , views.editar_profesor , name="editar_profesor"),
    path("elimina_alumno/<int:id>", views.elimina_alumno , name="elimina_alumno"),
    path("editar_alumno/<int:id>" , views.editar_alumno , name="editar_alumno"),
    path("login", views.login_request , name="login"),
    path("register", views.register , name="register"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editarPerfil" , views.editarPerfil , name="EditarPerfil"),
    path("editarPerfil", views.editarPerfil , name= "EditarPerfil")
]

