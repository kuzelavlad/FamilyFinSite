from django.db import models


class BaseDateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category_of_expenses(models.Model):
    title = models.CharField(verbose_name="Наименование Категории", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Expenses(models.Model):
    CURRENCY_CHOICES = (
        ("USD", "USD"),
        ("EUR", "EUR"),
        ("BYN", "BYN"),

    )

    category = models.ForeignKey(
        Category_of_expenses,
        on_delete=models.CASCADE,
        verbose_name="Наименование Категории Расхода"
    )
    amount = models.DecimalField(verbose_name="Сумма", max_digits=10, decimal_places=2)
    currency = models.CharField(verbose_name="Валюта", choices=CURRENCY_CHOICES, max_length=5)
    comment = models.CharField(verbose_name="Комментарий",
                               max_length=255,
                               null=True,
                               blank=True
                               )

    def __str__(self):
        return f'{self.category}{self.amount}'

    class Meta:
        verbose_name = "Расход"
        verbose_name_plural = "Расходы"
