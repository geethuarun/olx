from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from autos.forms import VehicleCreateForm,RegistrationForm,LoginForm
from django.views.generic import View,TemplateView,ListView,DetailView,UpdateView
from autos.models import Cars
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator

# Create your views here.
def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper



def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kwargs):
         form=RegistrationForm(request.POST)
         if form.is_valid():
             form.save()
             messages.success(request,"Registration successfully completed!!!!!")
             return redirect("signin")
         else:
             messages.error(request,"Registration failed....")
             return render(request,"registration.html",{"form":form})
    

# class SignUpView(View):
#     def get(self,request,*args,**kwargs):
#         form=RegistrationForm()
#         return render(request,"registration.html",{"form":form})
    
#     def post(self,request,*args,**kwargs):
#         form=RegistrationForm(request.POST)
#         if form.is_valid():
#             User.objects.create_user(**form.cleaned_data)
#             return redirect("signin")
#         else:
#             return render(request,"registration.html",{"form":form})
        
class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"Successfully login")
                return redirect("index")
            else:
                messages.error(request,"invalid credentials")
                return render(request,"login.html",{"form":form})
            
@method_decorator(signin_required,name="dispatch")           
class IndexView(TemplateView):
    template_name="index.html"
    def get(self,request,*args,**kwargs):
        form=VehicleCreateForm()
        qs=Cars.objects.filter(user=request.user)
        return render(request,self.template_name,{"form":form,"vehicles":qs})
    def post(self,request,*args,**kwargs):
        form=VehicleCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            Cars.objects.create(**form.cleaned_data,user=request.user)
            return redirect("index")
        else:
            return redirect("index")




@method_decorator(signin_required,name="dispatch")
class VehicleCreateView(View):
    def get(self,request,*args,**kwargs):
        form=VehicleCreateForm()
        return render(request,"vehicle_create.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=VehicleCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            Cars.objects.create(**form.cleaned_data,user=request.user)
            return redirect("veh-list")
        else:
            return render(request,"vehicle_create.html",{"form":form})
        
@method_decorator(signin_required,name="dispatch")
class VehicleListView(ListView):
    template_name="vehicle_list.html"
    context_object_name="vehicles"
    model=Cars
    def get_queryset(self):
        qs=Cars.objects.filter(user=self.request.user)
        return qs

    # def get(self,request,*args,**kwargs):
    #     qs=Cars.objects.all()
    #     return render(request,"vehicle_list.html",{"vehicles":qs})
    
@method_decorator(signin_required,name="dispatch")
class VehicleDetailView(DetailView):
    template_name="vehicle_detail.html"
    context_object_name="vehicle"
    model=Cars
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     qs=Cars.objects.get(id=id)
    #     return render(request,"vehicle_detail.html",{"vehicle":qs})
@method_decorator(signin_required,name="dispatch")   
class VehicleUpdateView(UpdateView):
    template_name="vehicle_update.html"
    form_class=VehicleCreateForm
    model=Cars
    success_url=reverse_lazy("veh-list")
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     obj=Cars.objects.get(id=id)
    #     form=VehicleCreateForm(instance=obj)
    #     return render(request,"vehicle_update.html",{"form":form})
    
    # def post(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     obj=Cars.objects.get(id=id)
    #     form=VehicleCreateForm(request.POST,instance=obj,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("veh-list")
    #     else:
    #         return render(request,"vehicle_update.html",{"form":form})
        
# class VehicleDeleteView(View):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         Cars.objects.get(id=id).delete()
#         return redirect("veh-list")
@signin_required
def remove_vehicle(request,*args,**kwargs):
    id=kwargs.get("pk")
    Cars.objects.filter(id=id).delete()
    return redirect("veh-list")




