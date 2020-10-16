from django.urls import path

from . import views

from recipes.views import MyRecipeListView

urlpatterns = [
    path('profile/edit/', views.ProfileUpdate.as_view(), name='profile_edit'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('my_recipes/', MyRecipeListView.as_view(), name='users_recipe'),
]
