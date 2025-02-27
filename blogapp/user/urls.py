from django.urls import path
from . import views

urlpatterns = [
    # path('home/', views.rendering_first_template, name='home'),
    # path('extend/', views.call_extend, name='extend')
    
    #  path('login/'),
    path('register/', views.register),
    path('login/', views.login)
]