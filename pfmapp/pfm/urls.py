from django.urls import path
from .views import expense_list, income_list, budget_list

urlpatterns = [
    path('expenses/', expense_list, name='expense_list'),
    path('incomes/', income_list, name='income_list'),
    path('budgets/', budget_list, name='budget_list'),
]
