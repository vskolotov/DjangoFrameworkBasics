from django.urls import path
from adminapp.views import user


urlpatterns = [
    path('users/create/', user.UsersCreateView.as_view(), name='user_create'),
    path('users/read/', user.UsersListView.as_view(), name='users'),
    path('users/update/<int:pk>/', user.UserUpdate.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', user.UserDelete.as_view(), name='user_delete'),
]