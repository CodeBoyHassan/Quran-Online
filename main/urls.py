from django.urls import path 
from . import views as v 

urlpatterns = [
    path('', v.home, name="home"),
    path('apply/', v.register, name="register"),
    path('faq/', v.faq, name="faq"),
    path('success/', v.success, name="success")
]
