from django.shortcuts import render , redirect
from django.http import HttpResponse 
from .models import Item
from .forms import ItemForm
from django.template import loader
from django.contrib.auth.decorators import login_required
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


@login_required
def index(request):
    item_list = Item.objects.all()
    context ={
        'item_list' : item_list,
    }
    return render(request,'food/index.html',context)


def item(request):
    
    return HttpResponse ('<h1><u>This is an item view</u></h1> ')


def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    #return HttpResponse("This is item no/id %s" %item_id)
    return render(request,'food/detail.html',context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() :
        form.save()
        return redirect('food:index')  # this means to follow the path that the name is "index", and the namespace= "food" ans defined in the url views by app_name=food
    return render(request,'food/item-form.html',{'form': form}) # the last part is the context

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