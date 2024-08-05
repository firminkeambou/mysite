from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Item(models.Model):   # this class will create a table called Item
    # by  default, when you query this model, it will returns with 'Item.objects.all()' something like "<QuerySet [<Item: Item object (1)>, <Item: Item object (2)>]>", if you want a different behavior, for example the name of the item, Do as follows:
    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=18) # this line of code creates relationship between  USER and item models, "on_delete" means, if the user is deleted, the item is automatically deleted as well
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price= models.IntegerField()
    item_image= models.CharField(max_length=500 ,default="https://www.shutterstock.com/shutterstock/photos/2145440019/display_1500/stock-vector-exciting-new-cafe-bar-restaurant-menu-coming-soon-flat-design-2145440019.jpg") # image url is stored over here; if it weren't a link, you would have needed to install  pillow package

   # the following line is because  in case of a class based view, we also need to mention the Url where we want django to redirect Us when the item is created
    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})  # "food:detail" is where we want to be redirected
    
