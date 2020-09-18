from django.urls import reverse_lazy
from django.views import generic
from django.conf import settings
from django.shortcuts import get_object_or_404

from .forms import CustomUserCreationForm

from .models import UserProfile, CustomUser

from .signals import *

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ProfileView(generic.detail.DetailView):
    model = UserProfile
    template_name = 'profile.html'

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)

class ProfileUpdate(generic.edit.UpdateView):
    model = UserProfile
    fields = ('username', 'first_name', 'last_name', 'image')
    template_name = 'profile_edit.html'

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)
