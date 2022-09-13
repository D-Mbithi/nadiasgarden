from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from pizza import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('order', views.order, name='order'),
    path('pizzas', views.pizzas, name='pizzas'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
]
