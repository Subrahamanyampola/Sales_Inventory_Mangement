# """sales_inventory_management_system URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/1.11/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.conf.urls import url, include
#     2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
# """
# from django.conf.urls import include, url
# from django.contrib import admin
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     url(r'^$', include('pages.urls')),
#     url(r'^pages/', include('pages.urls')),
#     url(r'^company/', include('company.urls')),
#     url(r'^type/', include('type.urls')),
#     url(r'^users/', include('users.urls')),
#     url(r'^products/', include('products.urls')),
#     url(r'^admin/', admin.site.urls),
# ]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
sales_inventory_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path # ✅ Updated import
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),  # ✅ Updated from url() to path()
    path('pages/', include('pages.urls')),
    path('company/', include('company.urls')),
    path('type/', include('type.urls')),
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),
]

# ✅ Static and media file serving
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
