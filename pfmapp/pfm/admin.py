from django.contrib import admin

from .models import Budget, Expense, Income

# Register your models here.
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'name', 'amount', 'date', 'category' )
    list_filter = ('user', 'date', 'category')
    search_fields = ('name', 'category', 'user__username')

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'amount', 'date', 'source')
    list_filter = ('user', 'date', 'source')
    search_fields = ('name', 'source', 'user__username')


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'month', 'start_date', 'end_date', 'allocated_amount')
    list_filter = ('user', 'month')
    search_fields = ('name', 'user__username')