from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import edit
from .models import Recipe, Comment, Ingredient

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
    )

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from django.db.models import Q
from django.db.models import Count

def like_view(request, pk):
    recipe = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    recipe.likes.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

# here im trying to add search functionality
def search(request):
    """implementing searching functionality to add ingredients
     to recipe in the future"""
    ingredient_name = request.GET.get('search')

    if ingredient_name:
        ingredients = Ingredient.objects.filter(Q(name__icontains=ingredient_name))
    else:
        ingredients = []

    return render(request, 'search.html', {'ingredients': ingredients})


class RecipeListView(LoginRequiredMixin, generic.ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, generic.detail.DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RecipeDetailView, self).get_context_data()
        recipe = get_object_or_404(Recipe, id=self.kwargs['pk'])
        total_likes = recipe.total_likes
        context["total_likes"] = total_likes
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
    fields = ('title', 'description', 'ingredients',)

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


class AddCommentView(edit.CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = ('text',)
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)


# special admin functionality for adding new info to database
class AddIngredientDataView(LoginRequiredMixin, edit.CreateView):
    """View for inserting new ingredients to our database"""
    model = Ingredient
    template_name = 'add_ingredient.html'
    fields = ('name', 'proteins', 'fats', 'carbohydrates')
    success_url = reverse_lazy('recipe_list')


class TopRecipeListView(LoginRequiredMixin, generic.ListView):
    """View to get queryset of top liked recipes"""
    model = Recipe
    template_name = 'top_recipe.html'

    def get_queryset(self):
        return Recipe.objects.annotate(likes_count=Count('likes')).order_by('-likes_count')
