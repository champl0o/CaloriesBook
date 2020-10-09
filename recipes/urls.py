from django.urls import path, include
from .views import (
    RecipeListView,
    RecipeDetailView,
    RecipeUpdateView,
    RecipeCreateView,
    RecipeDeleteView,
)

urlpatterns = [
    path('<int:pk>/edit/',
        RecipeUpdateView.as_view(), name='recipe_edit'),
    path('<int:pk>/',
        RecipeDetailView.as_view(), name='recipe_detail'),
    path('<int:pk>/delete/',
        RecipeDeleteView.as_view(), name='recipe_delete'),
    path('new/',
        RecipeCreateView.as_view(), name='recipe_new'),
    path('', RecipeListView.as_view(), name='recipe_list')
]
