"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import os
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

# from pages.views import home_view

from rest_framework import routers
# import sys
# sys.path.append('/products')
from products import views

# this_path = os.path.join(settings.BASE_DIR, 'src/products')
# import sys
# sys.path.append("..")
# from ..products.views import ProductViewset

# from src.products.views import ProductViewset

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
# router.register(r'p', views.PViewSet, basename='p')


urlpatterns = [
  # path('home/', home_view, name='home'),
  path('admin/', admin.site.urls),
  path('api/', include(router.urls))
]
