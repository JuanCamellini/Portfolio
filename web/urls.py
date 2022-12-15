from django.contrib import admin
from django.urls import path, include

from .views import home, thanks

urlpatterns = [
    path("",home,name="home"),
    path("thanks/", thanks, name="thanks")

]


""" agregar arriba de section id=contact

 <!-- Project section -->
<!--     {{ portfolio}} --> 
   <!-- Portfolio modal -->
<!--     {{ modal-portfolio}} -->
    <!-- Skillset section -->
<!--     {{ skillset}} --> 
   <!-- Experience section -->
    <!-- Resume modal -->
<!--     {{ modal-resume}} --> 
   <!-- Contact --> 
    """