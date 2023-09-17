from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from main.forms import ItemForm
from django.urls import reverse
from django.shortcuts import render
from main.models import Item

# Create your views here.
def show_main(request):
    items = Item.objects.all()
    total = 0
    for item in items:
        total += item.amount
    context = {
        'name': 'Charger Laptop',
        'amount': '3',
        'description': 'Charger laptop Acer Nitro, dengan kecepatan charge yang super cepat!',
        'category': 'Aksesoris Laptop',
        'power': '19V-3.42A',
        'price': 'Rp. 600.000,00',
        'expiry_date': 'none',
        'items': items,
        'total': total
    }

    return render(request, "daftar.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")