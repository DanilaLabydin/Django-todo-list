from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListListView.as_view(), name='index'),
    path('list/<int:list_id>/', views.ItemListView.as_view(), name='list')
    # crud patterns for ToDoList
    path('list/add/', views.ListCreate.as_view(), name='list_add'),
    # crud patterns for ToDoItems
    path(
        'list/<int:list_id>/item/add/',
        views.ItemCreate.as_view(),
        name='item-add',
    ),
    path(
        'list/<int:list_id>/item/<int:pk>/',
        views.ItemUpdate.as_view(),
        name='item-update'
    ),
]
