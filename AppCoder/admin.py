from django.contrib import admin
from AppCoder.models import Post_curso, Post_profesor, Post_estudiante

admin.site.register(Post_estudiante)

admin.site.register(Post_curso)

admin.site.register(Post_profesor)