from django.shortcuts import render

# Create your views here.
def store(request):
    return render(request, "store.html")
def cart(request):
    return render(request, "cart.html")
def main(request):
    return render(request, "main.html")
def checkout(request):
    return render(request, "checkout.html")