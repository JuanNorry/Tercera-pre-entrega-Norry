"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppCoder.views import index, curso, estudiante, profesor, agregar_post_curso, agregar_post_estudiante, agregar_post_profesor,buscar_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('template-curso', curso, name="template-curso"),
    path('template-estudiante', estudiante, name="template-estudiante"),
    path('template-profesor', profesor, name="template-profesor"),
    path('agregar_post/curso', agregar_post_curso, name="agregar-post-curso"),
    path('agregar_post/estudiante', agregar_post_estudiante, name="agregar-post-estudiante"),
    path('agregar_post/profesor', agregar_post_profesor, name="agregar-post-profesor"),
    path('buscar_post', buscar_post, name="buscar-post")
]
