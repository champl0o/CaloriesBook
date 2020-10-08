from django.db import models
from django.contrib.auth import get_user_model

from django.urls import reverse

from django.utils.timezone import now

class Recipe(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, verbose_name='Назва рецепту')
    pub_date = models.DateTimeField(default=now, editable=False)
    body = models.TextField(verbose_name='Опис')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])
