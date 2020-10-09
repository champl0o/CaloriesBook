from django.shortcuts import render
from django.views import generic
from django.views.generic import edit
from .models import Recipe

from django.urls import reverse_lazy

# Create your views here.
class RecipeListView(generic.ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(generic.detail.DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

class RecipeUpdateView(edit.UpdateView):
    model = Recipe
    template_name = 'recipe_edit.html'
    fields = ('title', 'description',)

class RecipeCreateView(edit.CreateView):
    model = Recipe
    template_name = 'recipe_new.html'
    fields = ('title', 'description',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeDeleteView(edit.DeleteView):
    model = Recipe
    template_name = 'recipe_delete.html'
    success_url = reverse_lazy('recipe_list')

class MyRecipeListView(generic.ListView):
    model = Recipe
    template_name = 'users_recipe.html'
