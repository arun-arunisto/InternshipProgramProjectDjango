from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('candidate_signup/', views.candidate_signup, name="candidate_signup"),
    path('candidate_login/', views.candidate_login, name="candidate_login"),
    path('application_form/', views.application_form, name="application_form"),
    path('candidate_profile/<str:username>/', views.candidate_profile, name="candidate_profile"),
    path('change_password/', views.change_password, name="change_password"),
    path('candidate_logout/', views.candidate_logout, name="candidate_logout")
]