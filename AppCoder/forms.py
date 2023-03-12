from django import forms
from AppCoder.models import Post_curso, Post_profesor, Post_estudiante

class Postform_curso(forms.ModelForm):
    class Meta:
        model = Post_curso
        fields = '__all__'

class Postform_estudiante(forms.ModelForm):
    class Meta:
        model = Post_estudiante
        fields = '__all__'

class Postform_profesor(forms.ModelForm):
    class Meta:
        model = Post_profesor
        fields = '__all__'
