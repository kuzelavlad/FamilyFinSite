from django.contrib import admin
from expenses.models import Category_of_expenses, Expenses


@admin.register(Category_of_expenses)
class Category_of_expensesAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = [
        "category",
        "amount",
        "currency",
    ]
