from django.core.paginator import Paginator
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from shop.models import ProductCategory, Product, Cart
from .forms import ReviewForm, SortForm


class Home(ListView):
    """Render home page"""
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nadin Store'
        return context


class About(ListView):
    """Render about page"""
    model = Product
    template_name = 'shop/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nadin Shop - About Page'
        return context


def shop(request, pk=None, page=1):
    context = {
        'title': 'Nadin Shop - Product Listing Page',
        'categories': ProductCategory.objects.all(),
    }
    if pk:
        context.update({'category_name': ProductCategory.objects.get(id=pk)})
    else:
        context.update({'category': Product.objects.all()})

    # pagination block starts
    products = Product.objects.filter(published=True)
    paginator = Paginator(products, 6) # 3 items on every page
    products_paginator = paginator.page(page)
    context.update({'products': products_paginator})
    # pagination block ends

    return render(request, 'shop/shop.html', context)


class ProductView(DetailView):
    """Personal product page"""
    model = Product
    template_name = 'shop/shop-single.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nadin Shop - Product Detail Page'
        context['categories'] = ProductCategory.objects.all()
        context['products'] = Product.objects.all()
        return context

# def shop_single(request, pk):
#     """Personal product page"""
#     context = {
#         'title': 'Nadin Shop - Product Detail Page',
#         'categories': ProductCategory.objects.all(),
#         'products': Product.objects.all(),
#         'product': Product.objects.get(pk=pk),
#     }
#     return render(request, 'shop/shop-single.html', context)


class Contact(ListView):
    """Render contact page"""
    model = Product
    template_name = 'shop/contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nadin Shop - Contact'
        return context

# def contact(request):
#     context = {
#         'title': 'Nadin Shop - Contact',
#     }
#     return render(request, 'shop/contact.html', context)


class Search(ListView):
    """Searching products"""
    model = Product

    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context


def cart_add(request, product_id):
    """Add products in cart"""
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    carts = Cart.objects.filter(user=request.user, product=product)

    if not carts.exists():
        Cart.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        cart = carts.first()
        cart.quantity += 1
        cart.save()
        return HttpResponseRedirect(current_page)


def cart_delete(request, id):
    """Delete products in cart"""
    cart = Cart.objects.get(id=id)
    if cart.quantity > 1:
        cart.quantity -= 1
        cart.save()
    else:
        cart.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def reviews(request):
    return render(request, 'shop/reviews.html')


class AddReview(View):
    """Add reviews"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)

        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.save()
        return redirect("/")


def sort_products(request):
    sort_form = SortForm(request.POST)
    products = Product.objects.filter(published=True)
    if sort_form.is_valid():
        needed_sort = sort_form.cleaned_data.get("sort_form")
        if needed_sort == "price_lth":
            products = products.order_by("price")
        elif needed_sort == "price_htl":
            products = products.order_by("-price")
        elif needed_sort == "a-z":
            products = products.order_by("word")
