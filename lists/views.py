from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List
from lists.forms import ItemForm

# Create your views here.
def home_page(request):
    items = Item.objects.all()
    return render(request, "home.html", {"form": ItemForm()})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, "list.html", {"list": list_})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST["text"], list=list_)
    return redirect(f"/lists/{list_.id}/")


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST["text"], list=list_)
    return redirect(f"/lists/{list_.id}/")
