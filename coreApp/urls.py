from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('pendidikan/', views.pendidikan, name='pendidikan'),
    path('pendidikan-input/', views.pendidikanInput, name='pendidikan-input'), 
    path('pendidikan-delete/<str:pk>/', views.pendidikanDelete, name='pendidikan-delete'), 

    path('jabatan/', views.jabatan, name='jabatan'),
    path('jabatan-input/', views.jabatanInput, name='jabatan-input'), 
    path('jabatan-delete/<str:pk>/', views.jabatanDelete, name='jabatan-delete'), 

    path('pegawai/', views.pegawai, name='pegawai'),
    path('pegawai-input/', views.pegawaiInput, name='pegawai-input'), 
    path('pegawai-delete/<str:pk>/', views.pegawaiDelete, name='pegawai-delete'), 
    path('pegawai-profil/<str:pk>/', views.pegawaiProfil, name='pegawai-profil'), 

]