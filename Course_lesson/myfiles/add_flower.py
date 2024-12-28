from django import forms
from pydantic.v1.errors import cls_kwargs

from .models import Course
class Gullarforms(forms.Form):
    title = forms.CharField(max_length=150,widget=forms.TextInput(attrs={
        "placeholder":"Nomini kiriting",
        "class":"form-control"
    }),label="Nomi")
    content = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder":"Matnini kiriting",
        "class":"form-control"
    }),required=False)
    photo = forms.ImageField(widget=forms.FileInput(attrs={
        "class":"form-control"
    }),required=False)
    category = forms.ModelChoiceField(queryset=Course.objects.all(),widget=forms.Select(attrs={
        "class":"form-select"
    }))
    published = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        "class":"form-check-input",
        "checked":"checked"
    }))

class Registerform(forms.Form):
        username = forms.CharField(min_length=8,widget=forms.TextInput())
        email = forms.EmailField(widget=forms.EmailInput())
        password = forms.CharField(min_length=8,widget=forms.PasswordInput())
        password_repeat = forms.CharField(min_length=8,widget=forms.PasswordInput())


class Loginform(forms.Form):
    username = forms.CharField(max_length=50,widget=forms.TextInput())
    password = forms.CharField(max_length=50,widget=forms.PasswordInput())





