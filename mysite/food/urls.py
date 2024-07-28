from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'food'  # this set the namespace and all named defined in here are only available for this app, example 'food:update_item'

urlpatterns = [
    # /food  # the following link still work, it's based on function based views
    # path('', views.index,name='index'),   # index contains all items, this is based on function based views

    # index path using class based view, don't forget to add "as_view() in the end" because , this is the particularity of class based view
    path('', login_required(views.IndexClassView.as_view()),
         name='index'),   # index contains all items

    path('item/', views.item, name='item'),    # get all item

    # /food/item/i based on function based view

          #  path('item/<int:item_id>/', views.detail,
                    #  name='detail'),  # get specific item
    
    # /food/item/i  based on class views
    path('item/<int:pk>/', views.DetailClassView.as_view(),
         name='detail'),  # get specific item
    # /food/add
    path('add', views.create_item, name='create_item'),
    # edit item
    path('update/<int:item_id>/', views.update_item, name='update_item'),
    # delete item

    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
