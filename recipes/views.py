from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import edit
from .models import Recipe

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
    )

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

def LikeView(request, pk):
    recipe = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    recipe.likes.add(request.user)
    return HttpResponseRedirect(reverse('recipe_detail', args=[str(pk)]))

# Create your views here.
class RecipeListView(LoginRequiredMixin, generic.ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(LoginRequiredMixin, generic.detail.DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RecipeDetailView, self).get_context_data()
        customRecipeInstance = get_object_or_404(Recipe, id=self.kwargs['pk'])
        total_likes = customRecipeInstance.total_likes()
        context["total_likes"] = total_likes
        template_name = 'recipe_detail.html'
        return context

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
