from django.urls import path
from .views import (
    ExpenseListCreateView, ExpenseDetailView,
    IncomeListCreateView, IncomeDetailView,
    BudgetListCreateView, BudgetDetailView,
    DashboardView
)

urlpatterns = [
    # Expenses
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    

    # Incomes
    path('incomes/', IncomeListCreateView.as_view(), name='income-list-create'),
    path('incomes/<int:pk>/', IncomeDetailView.as_view(), name='income-detail'),

    # Budgets
    path('budgets/', BudgetListCreateView.as_view(), name='budget-list-create'),
    path('budgets/<int:pk>/', BudgetDetailView.as_view(), name='budget-detail'),

    # Dashboard
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
