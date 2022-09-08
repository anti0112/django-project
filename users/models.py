from msilib.schema import _Validation
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.core.exceptions import ValidationError


def check_birthday(value:date):
    if date.today().year - value.year < 9:
        raise ValidationError(f"Your age must be more than 9 years old")

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return self.name


class User(AbstractUser):
    MEMBER = 'member'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLES = [
        ("member", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Админ"),
    ]

    role = models.CharField(max_length=9, choices=ROLES, default=MEMBER)
    age = models.PositiveIntegerField(null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    birth_date = models.DateTimeField(auto_now_add=True, null=True, validators=[check_birthday])

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
    