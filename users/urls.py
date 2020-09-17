from django.urls import path

from . import views

urlpatterns = [
    path('profile/edit/', views.ProfileUpdate.as_view(), name='profile_edit'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
