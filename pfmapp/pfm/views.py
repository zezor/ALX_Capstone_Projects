from django.shortcuts import render
from .models import Expense, Income, Budget

# Create your views here.


def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'pfm/expense_list.html', {'expenses': expenses})

def income_list(request):
    incomes = Income.objects.filter(user=request.user)
    return render(request, 'pfm/income_list.html', {'incomes': incomes})

def budget_list(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'pfm/budget_list.html', {'budgets': budgets})