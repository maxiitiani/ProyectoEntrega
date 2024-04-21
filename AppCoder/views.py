from django.shortcuts import render
from AppCoder.models import Curso
from AppCoder.models import Alumno
from AppCoder.models import Profesor
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario, UserEditForm, Alumno_formulario, Profesor_formulario
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, authenticate



# Create your views here.

def inicio(request):
    return render( request , "padre.html")

def alta_curso(request,nombre):
    curso = Curso(nombre=nombre , camada=234512)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)

def alta_profesor(request,nombre):
    profesor = Profesor(nombre=nombre , apellido=234512)
    profesor.save()
    texto = f"Se guardo en la BD el profesor: {profesor.nombre} {profesor.apellido}"
    return HttpResponse(texto)

def alta_alumno(request,nombre):
    alumno = Alumno(nombre=nombre , apellido=234512)
    alumno.save()
    texto = f"Se guardo en la BD el alumno: {alumno.nombre} {alumno.apellido}"
    return HttpResponse(texto)

def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def ver_profesores(request):
    profesores = Profesor.objects.all()
    dicc = {"profesores": profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    dicc = {"alumnos": alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def comentarios(request):
    return render( request , "comentario.html")

def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request , "formulario.html")


    return render(request , "formulario.html")

def alumno_formulario(request):

    if request.method == "POST":

        mi_formulario1 = Alumno_formulario( request.POST )

        if mi_formulario1.is_valid():
            datos = mi_formulario1.cleaned_data
            alumno = Alumno( nombre=datos["nombre"] , apellido=datos["apellido"])
            alumno.save()
            return render(request , "form_alumno.html")


    return render(request , "form_alumno.html")

def profesor_formulario(request):

    if request.method == "POST":

        mi_formulario2 = Profesor_formulario( request.POST )

        if mi_formulario2.is_valid():
            datos = mi_formulario2.cleaned_data
            profesor = Profesor( nombre=datos["nombre"] , apellido=datos["apellido"])
            profesor.save()
            return render(request , "form_profesor.html")


    return render(request , "form_profesor.html")


def buscar_curso(request):

    return render(request, "buscar_curso.html")



def buscar(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")

def buscar_alumno(request):

    return render(request, "buscar_alumno.html")

def buscar_alum(request):

    if request.POST["nombre"]:
        nombre = request.POST["nombre"]
        alumnos = Alumno.objects.filter(nombre__icontains= nombre)
        return render( request , "busqueda_alum.html" , {"alumno":alumnos})
    else:
        return HttpResponse("Ingrese el nombre del Alumno")

def buscar_profesor(request):

    return render(request, "buscar_profesor.html")

def buscar_prof(request):

    if request.POST["nombre"]:
        nombre = request.POST["nombre"]
        profesores = Profesor.objects.filter(nombre__icontains= nombre)
        return render( request , "busqueda_prof.html" , {"profesor":profesores})
    else:
        return HttpResponse("Ingrese el nombre del Profesor")


def busquedas(request):
    return render( request , "busquedas.html")

def elimina_curso(request , id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()

    return render(request , "cursos.html" , {"cursos":curso})

def editar(request , id):

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()

            curso = Curso.objects.all()

            return render(request , "cursos.html" , {"cursos":curso})


        
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})
    
    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})


def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request , user)
                return render(request, "inicio.html" , {"mensaje":f"Bienvenido/a {usuario}", "Usuario":f"{usuario}"})
            else:
                return HttpResponse(f"Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")


    form = AuthenticationForm()
    return render( request , "login.html" , {"form":form})


def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")
        

    else:
        form = UserCreationForm()
    return render(request , "registro.html" , {"form":form})


def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        pass

    else:
        miFormulario = UserEditForm(initial={"email":usuario.email})
    
    return render( request , "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})


