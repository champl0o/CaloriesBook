from django.db import models
from django.contrib.auth import get_user_model

from django.urls import reverse

from django.utils.timezone import now

class Recipe(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, verbose_name='Назва рецепту')
    pub_date = models.DateTimeField(default=now, editable=False)
    description = models.TextField(verbose_name='Опис')
    likes = models.ManyToManyField(get_user_model(), related_name='recipe_likes')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(default=now, editable=False)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('recipe_list')
