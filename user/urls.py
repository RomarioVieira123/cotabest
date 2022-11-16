from django.urls import path
from user.views import UserView, RegisterView, UsersView, GroupsView, GroupView, PermissionsView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('user/', UserView.as_view()),
    path('users/', UsersView.as_view()),
    path('user/<int:pk>', UserView.as_view()),
    path('groups/', GroupsView.as_view()),
    path('group/<int:pk>', GroupView.as_view()),
    path('create-group', GroupView.as_view()),
    path('permissions/', PermissionsView.as_view()),
]
