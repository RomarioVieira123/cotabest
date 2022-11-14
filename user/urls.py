from django.urls import path
from user.views import UserView, RegisterView, UsersView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('user/', UserView.as_view()),
    path('users/', UsersView.as_view()),
    path('user/<int:pk>', UserView.as_view()),
]

