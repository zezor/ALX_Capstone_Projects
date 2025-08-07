from django.shortcuts import render, redirect
from .models import Expense, Income, Budget
from .forms import ExpenseForm, IncomeForm, BudgetForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def add_expense(request):
    if request.method == 'POST':
        exp_form = ExpenseForm(request.POST)
        if exp_form.is_valid():
            expense = exp_form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expenses')

    else:
        exp_form = ExpenseForm()

    return render(request, 'pfm/add_expense.html', {'exp_form': exp_form})

@login_required
def add_income(request):
    if request.method == 'POST':
        inc_form = IncomeForm(request.POST)
        if inc_form.is_valid():
            income = inc_form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('incomes')
    else:
        inc_form = IncomeForm()
    return render(request, 'pfm/add_income.html', {'inc_form': inc_form})

@login_required
def add_budget(request):
    if request.method == 'POST':
        bud_form = BudgetForm(request.POST)
        if bud_form.is_valid():
            budget = bud_form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('budgets')
    else:
        bud_form = BudgetForm()

    return render(request, 'pfm/add_budget.html', {'bud_form': bud_form})

@login_required
def delete_expense(request, pk):
    try:
        expense = Expense.objects.get(id=pk, user=request.user)
        expense.delete()
        return render(request, 'pfm/expense_deleted.html')
    except Expense.DoesNotExist:
        return render(request, 'pfm/expense_not_found.html')

@login_required    
def delete_income(request, pk):
    try:
        income = Income.objects.get(id=pk, user=request.user)
        income.delete()
        return render(request, 'pfm/income_deleted.html')
    except Income.DoesNotExist:
        return render(request, 'pfm/income_not_found.html') 


@login_required    
def update_expense(request, pk):
        expense = Expense.objects.get(id=pk, user=request.user)
        if request.method == 'POST':
            exp_form = ExpenseForm(request.POST, instance=expense)
            if exp_form.is_valid():
                exp_form.save()
                return redirect('expenses')
        else:
            exp_form = ExpenseForm(instance=expense)
        return render(request, 'pfm/update_expense.html', {'exp_form': exp_form})
 


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

