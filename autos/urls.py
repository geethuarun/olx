from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from autos.views import SignInView,SignUpView,signout_view,VehicleCreateView,\
    VehicleDetailView,VehicleListView,VehicleUpdateView,remove_vehicle,IndexView


urlpatterns = [
    path("add/",VehicleCreateView.as_view(),name="veh-add"),
    path("list/",VehicleListView.as_view(),name="veh-list"),
    path("<int:pk>/",VehicleDetailView.as_view(),name="veh-detail"),
    path("<int:pk>/change/",VehicleUpdateView.as_view(),name="veh-change"),
    path("<int:pk>/remove/",remove_vehicle,name="veh-delete"),
    path("registration",SignUpView.as_view(),name="register"),
    path("",SignInView.as_view(),name="signin"),
    path("signout",signout_view,name="signout"),
    path("index",IndexView.as_view(),name="index")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)