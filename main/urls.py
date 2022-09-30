from django.urls import path
from . import views
#from .views import database

urlpatterns=[
    path('', views.index ,name='index'),
    path('about', views.about ,name='about'),
    path('audit', views.audit ,name='audit'),
    path('database',views.database,name='database'),
    path('/detail/<int:pk>', views.detail ,name='detail'),
    path('graph', views.graph ,name='graph'),
]