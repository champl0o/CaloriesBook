from django.shortcuts import render
from django.views import generic
from django.views.generic import edit
from .models import Recipe

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
    )

from django.urls import reverse_lazy

# Create your views here.
class RecipeListView(LoginRequiredMixin, generic.ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(LoginRequiredMixin, generic.detail.DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, edit.UpdateView):
    model = Recipe
    template_name = 'recipe_edit.html'
    fields = ('title', 'description',)

    def test_func(self):
        recipe = self.get_object()
        return recipe.author == self.request.user

class RecipeCreateView(LoginRequiredMixin, edit.CreateView):
    model = Recipe
    template_name = 'recipe_new.html'
    fields = ('title', 'description',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, edit.DeleteView):
    model = Recipe
    template_name = 'recipe_delete.html'
    success_url = reverse_lazy('recipe_list')

    def test_func(self):
        recipe = self.get_object()
        return recipe.author == self.request.user

class MyRecipeListView(LoginRequiredMixin, generic.ListView):
    model = Recipe
    template_name = 'users_recipe.html'

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)
