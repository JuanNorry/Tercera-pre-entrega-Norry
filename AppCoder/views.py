from django.shortcuts import render
from AppCoder.models import Post_curso, Post_estudiante, Post_profesor
from AppCoder.forms import Postform_curso, Postform_estudiante, Postform_profesor

def index(request):
    return render(request, "AppCoder/index.html")

def curso(request):
    context = {
        "form": Postform_curso(),
#        "posts": Post_curso.objects.all(),
    }

    return render(request, "AppCoder/template_curso.html", context)

def estudiante(request):
    context = {
        "form": Postform_estudiante(),
    }
    return render(request, "AppCoder/template_estudiante.html", context)

def profesor(request):
    context = {
        "form": Postform_profesor(),
    }
    return render(request, "AppCoder/template_profesor.html", context)


def agregar_post_curso(request):
    post_form = Postform_curso(request.POST)
    post_form.save()

    context = {
        "form": Postform_curso(),
        "posts": Post_curso.objects.all(),
    }
    return render(request, "AppCoder/template_curso.html", context)


def agregar_post_estudiante(request):
    post_form = Postform_estudiante(request.POST)
    post_form.save()
    context = {
        "form": Postform_estudiante(),
    }
    return render(request, "AppCoder/template_estudiante.html", context)


def agregar_post_profesor(request):
    post_form = Postform_profesor(request.POST)
    post_form.save()
    context = {
        "form": Postform_profesor(),
    }
    return render(request, "AppCoder/template_profesor.html", context)


def buscar_post(request):
    criterio = request.GET.get("criterio")
    context = {
        "posts": Post_curso.objects.filter(curso__icontains=criterio).all(),
    }

    return render(request, "AppCoder/template_curso.html", context)