from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from .managers import CustomUserManager

from django.conf import settings

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 30, verbose_name = 'Ім\'я')
    last_name = models.CharField(max_length = 30, verbose_name = 'Прізвище')
    username = models.CharField(max_length = 30, blank=True, verbose_name = 'Нікнейм')
    image = models.ImageField(default='default-avatar.png', upload_to='profile_image', blank=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('profile')
