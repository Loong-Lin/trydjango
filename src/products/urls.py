from django.urls import path
from products.views import (product_detail_view,
                            product_create_view,
                            product_list)

app_name = 'products'
urlpatterns = [

    path('', product_list, name='product-list'),
    path('<int:id>/', product_detail_view, name='product-detail'),
    path('create/', product_create_view, name='product-create'),
]