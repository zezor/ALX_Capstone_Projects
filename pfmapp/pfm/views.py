from django.shortcuts import render
from .models import Expense, Income, Budget

# Create your views here.

def add_expense(request):
    if request.method == 'POST':
        exp_form = ExpenseForm(request.POST)
        # Logic to handle expense creation
        pass
    return render(request, 'pfm/add_expense.html')








def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    context = {
        'expenses': expenses
    }
    return render(request, 'pfm/expense_list.html', context)


def income_list(request):
    incomes = Income.objects.filter(user=request.user)
    context = {
        'incomes': incomes
    }
    return render(request, 'pfm/income_list.html', context)


def budget_list(request):
    budgets = Budget.objects.filter(user=request.user)
    context = {
        'budgets': budgets
    }
    return render(request, 'pfm/budget_list.html', context)

def home(request):
    return render(request, 'pfm/home.html')