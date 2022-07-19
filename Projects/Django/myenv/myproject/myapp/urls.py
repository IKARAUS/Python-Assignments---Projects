from operator import index
from django.urls import path
from . import views


urlpatterns = [

    path('',views.home,name='home'),
    path('doctor/',views.home,name='doctor'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'), 
    path('profile/',views.profile,name='profile'),  
    path('change-password/',views.change_password,name='change-password'),  
    path('edit-profile/',views.edit_profile,name='edit-profile'),
    path('addnotice/',views.add_notice,name='addnotice'),
]
