from django.urls import path
from . import views
urlpatterns = [
    path('expenses/', views.expense_list, name='expenses'),
    path('incomes/', views.income_list, name='incomes'),
    path('budgets/', views.budget_list, name='budgets'),
    # Add paths for add_income, add_budget, delete_expense, etc. as needed
    path('add_income', views.add_income, name='add_income'),
    path('add_budget', views.add_budget, name='add_budget'),
    path('delete_expense/<int:id>/', views.delete_expense, name='delete_expense'),
    path('delete_income/<int:id>/', views.delete_income, name='delete_income'),
    path('update_expense/<int:id>/', views.update_expense, name='update_expense'),
]
