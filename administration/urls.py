from django.urls import path
from .views import *

urlpatterns = [
    path('administrative_index/', administrative_index, name="adminstrative index"),
    path('administrative_signup/', administrative_signup, name="administrative signup"),
    path('administrative_home/', administrative_home, name="administrative home"),
    path('candidates_list/', candidates_list, name='candidates_list'),
    path('administrative_profile/', administrative_profile, name='administrative_profile'),
    path('selected_candidates/', selected_candidates, name='selected candidates'),
    path('rejected_candidates/', rejected_candidates, name='rejected candidates')
]