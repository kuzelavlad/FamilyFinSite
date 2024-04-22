from django.db import models


class BaseDateMixin(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(models.Model):

    first_name = models.CharField(verbose_name="Имя", max_length=20)
    last_name = models.CharField(verbose_name="Фамилия", max_length=20)
    email = models.EmailField(verbose_name="Электронная Почта", max_length=255)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

