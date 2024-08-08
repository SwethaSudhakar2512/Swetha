
from django.urls import path
from .views import UserList, InterestListCreate, InterestUpdate, MessageListCreate

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('interests/', InterestListCreate.as_view(), name='interest-list-create'),
    path('interests/<int:pk>/', InterestUpdate.as_view(), name='interest-update'),
    path('messages/', MessageListCreate.as_view(), name='message-list-create'),
]
