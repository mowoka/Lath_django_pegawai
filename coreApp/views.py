from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import JabatanForm, PendidikanForm, PegawaiForm
from .filters import PegawaiFilter, JabatanFilter, PendidikanFilter
from .models import*
from .decorators import unauthenticated_user

# Create your views here.



@unauthenticated_user
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password Incorrect')

    context = {}
    return render(request, 'coreApp/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):

    context = {}
    return render(request, 'coreApp/home.html', context)

@login_required(login_url='login')
def pendidikan(request):
    
    pendidikans = Pendidikan.objects.all()
    total_pendidikan = pendidikans.count()

    myFilter = PendidikanFilter(request.GET, queryset=pendidikans)
    pendidikans = myFilter.qs

    context = {'pendidikans':pendidikans, 'total_pendidikan':total_pendidikan, 'myFilter':myFilter}
    return render(request, 'coreApp/pendidikan.html', context)

@login_required(login_url='login')
def pendidikanInput(request):

    form = PendidikanForm()

    if request.method == 'POST':
        form = PendidikanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pendidikan')
        

    context = {'form':form}
    return render(request, 'coreApp/pendidikan-input.html', context)

@login_required(login_url='login')
def pendidikanDelete(request, pk):

    pendidikan = Pendidikan.objects.get(id=pk)

    if request.method == 'POST':
        pendidikan.delete()
        return redirect('pendidikan')

    context = {'pendidikan':pendidikan}
    return render(request, 'coreApp/pendidikan-delete.html', context)

@login_required(login_url='login')
def jabatan(request):
    
    jabatans = Jabatan.objects.all()
    total_jabatan = jabatans.count()

    myFilter = JabatanFilter(request.GET , queryset=jabatans)
    jabatans = myFilter.qs

    context = {'jabatans':jabatans, 'total_jabatan':total_jabatan, 'myFilter':myFilter}
    return render(request, 'coreApp/jabatan.html', context)

@login_required(login_url='login')
def jabatanInput(request):

    form = JabatanForm()
    
    if request.method == 'POST':
        form = JabatanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jabatan')

    context = {'form':form}
    return render(request, 'coreApp/jabatan-input.html', context)

@login_required(login_url='login')
def jabatanDelete(request, pk):

    jabatan = Jabatan.objects.get(id=pk)

    if request.method == 'POST':
        jabatan.delete()
        return redirect('jabatan')

    context = {'jabatan':jabatan}
    return render(request, 'coreApp/jabatan-delete.html', context)

@login_required(login_url='login')
def pegawai(request):
    
    pegawais = Pegawai.objects.all()
    total_pegawai = pegawais.count()

    myFilter = PegawaiFilter(request.GET, queryset=pegawais)
    pegawais = myFilter.qs

    context = {'pegawais':pegawais, 'total_pegawai':total_pegawai, 'myFilter':myFilter}
    return render(request, 'coreApp/pegawai.html', context)

@login_required(login_url='login')
def pegawaiInput(request):

    form = PegawaiForm()

    if request.method == 'POST':
        form = PegawaiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pegawai')

    context = {'form':form}
    return render(request, 'coreApp/pegawai-input.html', context)

@login_required(login_url='login')
def pegawaiProfil(request, pk):

    pegawai = Pegawai.objects.get(id=pk)

    context = {'pegawai':pegawai}
    return render(request, 'coreApp/pegawai-profil.html', context)

@login_required(login_url='login')
def pegawaiDelete(request, pk):
    
    pegawai = Pegawai.objects.get(id=pk)

    if request.method == 'POST':
        pegawai.delete()
        return redirect('pegawai')

    context = {'pegawai':pegawai}
    return render(request, 'coreApp/pegawai-delete.html', context)    