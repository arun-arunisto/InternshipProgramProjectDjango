from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('candidate_signup/', views.candidate_signup, name="candidate_signup"),
    path('candidate_login/', views.candidate_login, name="candidate_login"),
    path('application_form/', views.application_form, name="application_form"),
    path('application_status/', views.application_status, name="application_status")
]