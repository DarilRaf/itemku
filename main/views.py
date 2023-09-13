from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Charger Laptop',
        'amount': '3',
        'description': 'Charger laptop Acer Nitro, dengan kecepatan charge yang super cepat!',
        'category': 'Aksesoris Laptop',
        'power': '19V-3.42A',
        'price': 'Rp. 600.000,00',
        'expiry_date': 'none'
    }

    return render(request, "daftar.html", context)