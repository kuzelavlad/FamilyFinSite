from django.contrib import admin
from earnings.models import Category_of_earnings, Earnings


@admin.register(Category_of_earnings)
class Category_of_earningsAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Earnings)
class EarningsAdmin(admin.ModelAdmin):
    list_display = [
        "category",
        "amount",
        "currency",
    ]
