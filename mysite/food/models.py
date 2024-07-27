from django.db import models

# Create your models here.
class Item(models.Model):   # this class will create a table called Item
    # by  default, when you query this model, it will returns with 'Item.objects.all()' something like "<QuerySet [<Item: Item object (1)>, <Item: Item object (2)>]>", if you want a different behavior, for example the name of the item, Do as follows:
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price= models.IntegerField()
    item_image= models.CharField(max_length=500 ,default="https://www.shutterstock.com/shutterstock/photos/2145440019/display_1500/stock-vector-exciting-new-cafe-bar-restaurant-menu-coming-soon-flat-design-2145440019.jpg") # image url is stored over here; if it weren't a link, you would have needed to install  pillow package
