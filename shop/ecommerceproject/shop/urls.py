from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.allProdCat, name="allProdCat"),
    path('home/<slug:c_slug>/', views.allProdCat, name="product_by_category"),
    path('home/<slug:c_slug>/<slug:product_slug>/', views.proDetail, name="product_by_category")
]
