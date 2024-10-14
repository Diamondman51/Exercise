from django.urls import path

from .views import AddUser, AllUsers, DeleteUser, EditUser


urlpatterns = [
    path('add_user/', AddUser.as_view(), name="add_user"),
    path('', AllUsers.as_view(), name="all_users"),
    path('edit_user/<int:user_id>', EditUser.as_view(), name="edit_user"),
    path('delete_user/<int:user_id>', DeleteUser.as_view(), name="delete_user"),
]
