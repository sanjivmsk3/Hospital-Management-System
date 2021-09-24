from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic.base import View
from app.forms import *

# Create your views here.


class Home(View):
    def get(self, request):
        return render(request, 'base.html')

class Logins(View):
    def get(self, request):
        return render(request,'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(username=username, password=password)
        except:
            return redirect('login')

        if user is not None:
            login(request, user)
            if request.user.is_superuser is True:
                return redirect('superadmin')
            elif request.user.is_staff is True:
                return redirect('doctor')
            elif request.user.is_active is True:
                return redirect('staff')
            else:
                logout(request)
                return redirect('login')
        else:
            return redirect('login')

class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class SuperAdmin(LoginRequiredMixin,View):
    def get(self, request):
        if request.user.is_superuser is True:
            context = {
                'allBranch':Branch.objects.all(),
                'allDoctor':User.objects.filter(is_staff=True),
                'allStaff':User.objects.filter(is_active=True)
            }
            return render(request, 'admin/home.html',context)
        else:
            logout(request)
            return redirect('login')

from datetime import date, timedelta

class Doctor(LoginRequiredMixin,View):
    def get(self, request):
        if request.user.is_staff:

            context ={
                'datse':Paitent.objects.all(),
            }
            return render(request, 'doctor/home.html',context)
        else:
            logout(request)
            return redirect('login')


class AddDoctor(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_superuser is True:
            form = SignUpForm()
            return render(request, 'admin/add-doctor.html',{'forms':form})
        else:
            logout(request)
            return redirect('login')

    def post(self, request):
        if request.user.is_superuser is True:
            form = SignUpForm(request.POST or None)
            if form.is_valid():
                f = form.save(commit=False)
                f.is_staff = True
                f.save()
                return redirect('superadmin')
        else:
            logout(request)
            return redirect('login')


class AddStaff(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_superuser is True:
            form = SignUpForm()
            return render(request, 'admin/add-staff.html',{'forms':form})
        else:
            logout(request)
            return redirect('login')

    def post(self, request):
        if request.user.is_superuser is True:
            form = SignUpForm(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect('superadmin')
        else:
            logout(request)
            return redirect('login')


class AddBranch(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_superuser is True:
            form = BranchForm()
            return render(request, 'admin/add-branch.html',{'forms':form})
        else:
            logout(request)
            return redirect('login')

    def post(self, request):
        if request.user.is_superuser is True:
            form = BranchForm(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect('superadmin')
        else:
            logout(request)
            return redirect('login')


class AddPatient(LoginRequiredMixin, View):
    def get(self, request):
        form = PatientForm()
        return render(request, 'staff/add-patient.html',{'forms':form})


    def post(self, request):
        form = PatientForm(request.POST or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('staff')



class Staff(LoginRequiredMixin,View):
    def get(self, request):
        if request.user.is_active:
            context = {
                'allPatient':Paitent.objects.filter(user=request.user).order_by('-id')
            }
            return render(request, 'staff/home.html',context)
        else:
            logout(request)
            return redirect('login')

class AllPatient(LoginRequiredMixin,View):
    def get(self, request):
        if request.user.is_superuser:
            context = {
                'allPatient':Paitent.objects.all().order_by('-id')
            }
            return render(request, 'admin/all-patient.html',context)
        else:
            logout(request)
            return redirect('login')