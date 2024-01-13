from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('list/', views.list, name='list'),
    path('<int:id>', views.list_item, name='list_item'),
    path('edit_list/<int:id>', views.edit_list, name='edit_list'),
    path('delete_list/<int:id>', views.delete_list, name='delete_list'),
]
