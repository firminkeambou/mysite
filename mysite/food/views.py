from django.shortcuts import render , redirect
from django.http import HttpResponse 
from .models import Item
from .forms import ItemForm
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.
## first method for index view
'''def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html') # you don't need to add the directory named "templates"
    context ={
        'item_list' : item_list,

    }
    return HttpResponse (template.render(context,request))
    '''
## second method for index view (optimal)


@login_required  # decorator that means the connexion is mandatory
def index(request):
    item_list = Item.objects.all()
    context ={
        'item_list' : item_list,
    }
    return render(request,'food/index.html',context)

# As index view above just list a list of items , we can rewrite it using class based views  as follow



class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


##################
def item(request):
    
    return HttpResponse ('<h1><u>This is an item view</u></h1> ')


def detail(request,item_id):
   item = Item.objects.get(pk=item_id)
   context = {
       'item': item,
    }
    #return HttpResponse("This is item no/id %s" %item_id)
   return render(request,'food/detail.html',context)

# class based view for details
class DetailClassView(DetailView):
    model = Item
    template_name = 'food/detail.html'
    # as you can see, we don't need to pass a context any more, django will be able to identified a record  by using "object" or "item" (because we are dealing with Item Model) in the template
    #context_object_name = 'item' 

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() :
        form.save()
        return redirect('food:index')  # this means to follow the path that the name is "index", and the namespace= "food" ans defined in the url views by app_name=food
    return render(request,'food/item-form.html',{'form': form}) # the last part is the context

## class based for "create_item" so we can easily associate Apps
class CreateItem(CreateView):
    model = Item
    fields = ['item_name','item_desc','item_price','item_image']
    template_name = 'food/item-form.html'
    def form_valid(self,form):
        form.instance.user_name = self.request.user  # this is kind of association User

        return super().form_valid(form)


def update_item(request, item_id):
    item = Item.objects.get(pk=item_id)  # or  Item.objects.get(id=item_id)
    form = ItemForm(request.POST or None, instance=item) #this automatically fills form with data collected from the database
    context = {
        'item': item,
        'form': form,
    }

    if form.is_valid():
        form.save()
        # this means to follow the path that the name is "index", and the namespace= "food" ans defined in the url views by app_name=food
        return redirect('food:index')
    return render(request, 'food/item-form.html',context)


def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)  # or  Item.objects.get(id=item_id)
    # this automatically fills form with data collected from the database
    form = ItemForm(request.POST or None, instance=item)
    context = {
        'item': item,
        'form': form,
    }
    if request.method == 'POST':
        item.delete()
        # this means to follow the path that the name is "index", and the namespace= "food" ans defined in the url views by app_name=food
        return redirect('food:index')
    return render(request, 'food/item-delete.html', context)