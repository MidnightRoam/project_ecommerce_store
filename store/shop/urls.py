from django.urls import path

from .views import Home, About, shop, Contact, reviews, AddReview, cart_add, cart_delete, Search, ProductView

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('shop/', shop, name='shop'),
    path('category/<int:pk>/', shop, name='category'),
    # path('product/<int:pk>/', shop_single, name='shop-single'),
    path('contact/', Contact.as_view(), name='contact'),
    path('page/<int:page>/', shop, name='page'),
    path('product/<int:pk>/', ProductView.as_view(), name='shop-single'),
    path('reviews/', reviews, name='reviews'),
    path('reviews/<int:pk>/', AddReview.as_view(), name='add_review'),
    path('cart-add/<int:product_id>', cart_add, name='cart_add'),
    path('cart-delete/<int:id>', cart_delete, name='cart_delete'),
    path('shop/', Search.as_view(), name='search'),
]
