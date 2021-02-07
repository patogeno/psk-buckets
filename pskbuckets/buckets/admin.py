from django.contrib import admin
from safedelete.admin import SafeDeleteAdmin, highlight_deleted
from .models import Bucket, BankAccount, Category, Transaction


@admin.register(Bucket)
class BucketAdmin(SafeDeleteAdmin):
    list_display = (highlight_deleted, "name") + SafeDeleteAdmin.list_display
    list_filter = SafeDeleteAdmin.list_filter


@admin.register(BankAccount)
class BankAccountAdmin(SafeDeleteAdmin):
    list_display = (highlight_deleted, "name") + SafeDeleteAdmin.list_display
    list_filter = SafeDeleteAdmin.list_filter


@admin.register(Category)
class CategoryAdmin(SafeDeleteAdmin):
    list_display = (highlight_deleted, "name") + SafeDeleteAdmin.list_display
    list_filter = SafeDeleteAdmin.list_filter


@admin.register(Transaction)
class TransactionAdmin(SafeDeleteAdmin):
    list_display = (
        highlight_deleted,
        "name",
        "get_bucket",
    ) + SafeDeleteAdmin.list_display
    list_filter = (
        "bucket__name",
        "bucket__bank_account__name",
        "category__name",
    ) + SafeDeleteAdmin.list_filter

    def get_bucket(self, obj):
        return obj.bucket.name
