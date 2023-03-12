from AppCoder.models import Post_curso, Post_estudiante, Post_profesor

Post_curso(curso="Un curso",
     camada="Una camada",
     ).save()

Post_estudiante(nombre="Un nombre",
     apellido="Un apellido",
     email="Un email"
     ).save()

Post_profesor(nombre="Un nombre",
     apellido="Un apellido",
     profesion="Una profesion"
     ).save()