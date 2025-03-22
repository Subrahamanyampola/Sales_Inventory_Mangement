# from django.conf.urls import url
# from . import views

# urlpatterns = [
#     url(r'^$', views.listing, name="type-listing"),
#     url(r'^list$', views.lists, name="type-lists"),
#     url(r'^add$', views.add, name="add"),
#     url(r'^delete/(?P<id>\w{0,50})/$', views.delete, name="delete"),
#     url(r'^update/(?P<typeId>\w{0,50})/$', views.update, name="update"),
# ]
from django.urls import path  # Correct import for Django 4.x
from . import views

urlpatterns = [
    path('', views.listing, name="type-listing"),
    path('list', views.lists, name="type-lists"),
    path('add', views.add, name="add"),
    path('delete/<str:id>/', views.delete, name="delete"),
    path('update/<str:typeId>/', views.update, name="update"),
]
