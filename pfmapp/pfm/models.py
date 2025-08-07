from django.db import models

# Create your models here.



class Expense(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='expenses')
    name = models.CharField(max_length=100, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.amount} on {self.date}"


class Income(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='incomes')
    name = models.CharField(max_length=100, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField()
    source = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.amount} on {self.date}"

 
class Budget(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='budgets')
    name = models.CharField(max_length=100, blank=True)
    allocated_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    month = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.month} from {self.start_date} to {self.end_date}"