# from django.conf.urls import url
# from . import views

# urlpatterns = [
#     url(r'^$', views.products, name="products"),
#     url(r'^filters/(?P<typeID>\w{0,50})/$', views.product_filter, name="product_filter"),
#     url(r'^product-listing$', views.productlisting, name="productlisting"),
#     url(r'^product-inventory$', views.productinventory, name="productinventory"),
#     url(r'^payment$', views.payment, name="payment"),
#     url(r'^cart_listing$', views.cart_listing, name="cart_listing"),
#     url(r'^order-listing$', views.orderlisting, name="orderlisting"),
#     url(r'^order-items/(?P<orderID>\w{0,50})/$', views.order_items, name="order_items"),
#     url(r'^order-edit/(?P<orderID>\w{0,50})/$', views.order_edit, name="order_edit"),
#     url(r'^order-cancel/(?P<orderID>\w{0,50})/$', views.cancel_order, name="cancel_order"),
#     url(r'^add$', views.add, name="add"),
#     url(r'^product-details/(?P<productId>\w{0,50})/$', views.product_details, name="product_details"),
#     url(r'^update/(?P<productId>\w{0,50})/$', views.update, name="update"),
#     url(r'^cart-delete/(?P<itemId>\w{0,50})/$', views.delete_item, name="delete_item"),
#     url(r'^delete/(?P<prodId>\w{0,50})/$', views.delete, name="delete"),
#     url(r'^stock$', views.stock, name="stock"),
#     url(r'^deletestock/(?P<id>\w{0,50})/$', views.deletestock, name="deletestock"),
#     url(r'^order$', views.order, name="order"),
#     url(r'^companylisting$', views.companylisting, name="companylisting"),
#     url(r'^addcompany$', views.addcompany, name="addcompany"),
#     url(r'^deletecompany/(?P<id>\w{0,50})/$', views.deletecompany, name="deletecompany"),
# ]
from django.urls import path  # ✅ Correct import for Django 4.x
from . import views

urlpatterns = [
    path('', views.products, name="products"),
    path('filters/<str:typeID>/', views.product_filter, name="product_filter"),
    path('product-listing', views.productlisting, name="productlisting"),
    path('product-inventory', views.productinventory, name="productinventory"),
    path('payment', views.payment, name="payment"),
    path('cart_listing', views.cart_listing, name="cart_listing"),
    path('order-listing', views.orderlisting, name="orderlisting"),
    path('order-items/<str:orderID>/', views.order_items, name="order_items"),
    path('order-edit/<str:orderID>/', views.order_edit, name="order_edit"),
    path('order-cancel/<str:orderID>/', views.cancel_order, name="cancel_order"),
    path('add', views.add, name="add"),
    path('product-details/<str:productId>/', views.product_details, name="product_details"),
    path('update/<str:productId>/', views.update, name="update"),
    path('cart-delete/<str:itemId>/', views.delete_item, name="delete_item"),
    path('delete/<str:prodId>/', views.delete, name="delete"),
    path('stock', views.stock, name="stock"),
    path('deletestock/<str:id>/', views.deletestock, name="deletestock"),
    path('order', views.order, name="order"),
    path('companylisting', views.companylisting, name="companylisting"),
    path('addcompany', views.addcompany, name="addcompany"),
    path('deletecompany/<str:id>/', views.deletecompany, name="deletecompany"),
]
