from django.urls import path
from . import views
from views import food_list,food_detail, food_post , update_food

urlpatterns = [
    path('food', food_list, name='food_list'),
    path('food/<int:id>/', food_detail, name='food_detail'),
    path('food/create/', food_post, name='food_post'),
    path('food/update/<int:id>/', update_food, name='update_food'),

]