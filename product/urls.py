from django.urls import path

from product.views import ProductView, ProductsView, ProductSearchView

urlpatterns = [
    path('product/', ProductView.as_view()),
    path('products/', ProductsView.as_view()),
    path('product/<int:pk>', ProductView.as_view()),
    path('search/products/', ProductSearchView.as_view())
]

