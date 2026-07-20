from django.shortcuts import render, redirect
from django.template.context_processors import request
from shop.models import Product
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.shortcuts import get_object_or_404, redirect
from .models import Product
from .models import Order, OrderItem
from .forms import OrderForm


def index(request):
    products = Product.objects.all()
    context = {
        'title':'Shop_store',
        'products':products,
    }
    return render(request,'shop/index.html',context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "login.html", {
                "error": "Username yoki parol noto'g'ri."
            })

    return render(request, "login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Parollarni tekshirish
        if password1 != password2:
            return render(request, "shop/register.html", {
                "error": "Parollar bir xil emas."
            })

        # Username bandligini tekshirish
        if User.objects.filter(username=username).exists():
            return render(request, "shop/register.html", {
                "error": "Bu username band."
            })

        if User.objects.filter(email=email).exists():
            return render(request, "shop/register.html", {
                "error": "Bu email allaqachon ro'yxatdan o'tgan."
            })

        # Foydalanuvchini yaratish
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        login(request, user)
        return redirect("index")

    return render(request, "shop/register.html")


def logout_view(request):
    logout(request)
    return redirect("index")



def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)

    context = {
        'product':product,
    }

    return render(request,'shop/product_detail.html',context)

def cart(request):
    cart = request.session.get("cart", {})

    products = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)

        product.quantity = quantity
        product.subtotal = product.price * quantity

        total += product.subtotal
        products.append(product)

    return render(request, "shop/cart.html", {
        "products": products,
        "total": total
    })

def add_to_cart(request, pk):
    cart = request.session.get("cart", {})

    pk = str(pk)

    if pk in cart:
        cart[pk] += 1
    else:
        cart[pk] = 1

    request.session["cart"] = cart

    return redirect("cart")


def increase_quantity(request, pk):
    cart = request.session.get("cart", {})

    pk = str(pk)

    if pk in cart:
        cart[pk] += 1

    request.session["cart"] = cart

    return redirect("cart")


def decrease_quantity(request, pk):
    cart = request.session.get("cart", {})

    pk = str(pk)

    if pk in cart:

        if cart[pk] > 1:
            cart[pk] -= 1
        else:
            del cart[pk]

    request.session["cart"] = cart

    return redirect("cart")


def remove_from_cart(request, pk):
    cart = request.session.get("cart", {})

    pk = str(pk)

    if pk in cart:
        del cart[pk]

    request.session["cart"] = cart

    return redirect("cart")





def checkout(request):
    cart = request.session.get("cart", {})

    if not cart:
        return redirect("cart")

    total = 0

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():

            order = form.save(commit=False)

            for product_id, quantity in cart.items():

                product = Product.objects.get(id=product_id)

                total += product.price * quantity

            order.total_price = total

            order.save()

            for product_id, quantity in cart.items():

                product = Product.objects.get(id=product_id)

                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=product.price
                )

            request.session["cart"] = {}

            return redirect("index")

    else:

        form = OrderForm()

    return render(request,
                  "shop/checkout.html",
                  {"form": form})



def payment_success(request):
    return render(request, "shop/payment.html")