from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', login_page, name='login'),
    path('zapcas-list/', zapcas_list, name='zapcas_list'),
    path('create-zapcas/', create_zapcas, name='create_zapcas'),
    path('update-zapcas/<int:id>/', update_zapcas, name='update_zapcas'),
    path('delete-zapcas/<int:id>/', delete_zapcas, name='delete_zapcas'),
    path('logout/', logout, name="logout"),




    # path('search/', Search.as_view(), name='search'),


            
    # path('cars_list/', cars_list, name='cars_list'),
    # path('update_cars/<int:id>/', update_cars, name='update_cars'),
    # path('delete_cars/<int:id>/', delete_cars, name='delete_cars'),
]