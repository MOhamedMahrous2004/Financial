from django.urls import path
from . import views

urlpatterns = [
    path('transactions/', views.TransactionListCreate.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', views.TransactionDetail.as_view(), name='transaction-detail'),
]
