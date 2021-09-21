from django.urls import path
from app.views import *

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('login',Logins.as_view(),name='login'),
    path('logout',LogOut.as_view(),name='logout'),
    path('superadmin',SuperAdmin.as_view(),name='superadmin'),
    path('doctor',Doctor.as_view(),name='doctor'),
    path('add-doctor',AddDoctor.as_view(),name='add-doctor'),
    path('add-staff',AddStaff.as_view(),name='add-staff'),
    path('add-patient',AddPatient.as_view(),name='add-patient'),
    path('add-branch',AddBranch.as_view(),name='add-branch'),
    path('staff',Staff.as_view(),name='staff'),
    path('all-patient',AllPatient.as_view(),name='all-patient'),
]