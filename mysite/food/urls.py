from django.urls import path
from . import views

app_name = 'food'  # this set the namespace and all named defined in here are only available for this app, example 'food:update_item'

urlpatterns = [
    path('', views.index,name='index'),   # index contains all items
    path('item/', views.item,name='item'),    # get all item
    path('item/<int:item_id>/', views.detail,name='detail'),  #get specific item
    # add items
    path('add', views.create_item, name='create_item'),
    # edit item
    path('update/<int:item_id>/', views.update_item, name='update_item'),
    # delete item

    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
