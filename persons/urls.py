from django.urls import path
from . import views
#from .views import database

urlpatterns=[
    path('login', views.login_user ,name='login'),
    path('logout', views.logout_user ,name='logout'),
    path('superpage', views.superpage ,name='superpage'),
    path('/delete/<int:pk>', views.delete ,name='delete'),
    path('/edit/<int:pk>', views.edit ,name='edit'),
]