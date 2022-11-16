from django.urls import path
from cart.views import CartView, CartsView

urlpatterns = [
    path('cart/', CartView.as_view()),
    path('carts/', CartsView.as_view()),
    path('cart/<int:pk>', CartView.as_view())
]
