from django.urls import path
from .views import add_budget, delete_expense, add_income, expense_list, income_list, budget_list

urlpatterns = [
    path('expenses/', expense_list, name='expense_list'),
    path('incomes/', income_list, name='income_list'),
    path('budgets/', budget_list, name='budget_list'),
    # Add paths for add_income, add_budget, delete_expense, etc. as needed
    path('add_income/', add_income, name='add_income'),
    path('add_budget/', add_budget, name='add_budget'),
    path('delete_expense/<int:id>/', delete_expense, name='delete_expense'),
]
