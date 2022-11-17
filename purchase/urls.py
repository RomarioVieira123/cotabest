from django.urls import path

from purchase.views import PurchaseView

urlpatterns = [
    path('purchase/<int:pk>', PurchaseView.as_view()),
]

