from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE
import datetime

class BaseModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"({self.id}) {self.name}"

    class Meta:
        abstract = True


class BankAccount(BaseModel):
    description = models.TextField(max_length=256, blank=True, default="")


class Bucket(BaseModel):
    bank_account = models.ForeignKey(
        BankAccount, on_delete=models.CASCADE, related_name="transactions"
    )
    description = models.TextField(max_length=256, blank=True, default="")


class Category(BaseModel):
    description = models.TextField(max_length=256, blank=True, default="")

    class Meta:
        verbose_name_plural = "Categories"


class Transaction(BaseModel):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    bucket = models.ForeignKey(
        Bucket, on_delete=models.CASCADE, related_name="transactions"
    )

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="transactions"
    )
    is_real = models.BooleanField()
    datetime = models.DateTimeField(default=datetime.datetime.now)
