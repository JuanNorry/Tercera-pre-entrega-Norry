from django.db import models

class Post_curso(models.Model):
    curso = models.CharField(max_length=30)
    camada = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.id} - {self.curso}"
    
class Post_estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id} - {self.apellido}"

class Post_profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id} - {self.apellido}"
