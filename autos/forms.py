from django import forms
from autos.models import Cars
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=["username","email","password"]
#         widgets={
#             "username":forms.TextInput(attrs={"class":"form-control"}),
#             "email":forms.EmailInput(attrs={"class":"form-control"}),
#             "password":forms.PasswordInput(attrs={"class":"form-control"})}

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

        

class VehicleCreateForm(forms.ModelForm):

    class Meta:
        model=Cars
        fields=["make","address","mileage","no_of_owners","price","year","image"]
        widgets={"make":forms.TextInput(attrs={"class":"form-control"}),
                 "address":forms.Textarea(attrs={"class":"form-control","rows":3}),
                 "mileage":forms.TextInput(attrs={"class":"form-control"}),
                 "no_of_owners":forms.TextInput(attrs={"class":"form-control"}),
                 "price":forms.TextInput(attrs={"class":"form-control"}),
                  "year":forms.TextInput(attrs={"class":"form-control"})

                 }
