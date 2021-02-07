from rest_framework import serializers
from .models import Bucket, BankAccount, Category, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "created_date",
            "modified_date",
            "name",
            "amount",
            "bucket",
            "category",
            "is_real",
            "datetime",
        ]

class TransactionMiniBucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "name",
            "amount",
            "category",
            "is_real",
            "datetime",
        ]

class TransactionMiniCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "name",
            "amount",
            "bucket",
            "is_real",
            "datetime",
        ]


class BucketSerializer(serializers.ModelSerializer):
    transactions = TransactionMiniBucketSerializer(many=True, required=False)

    class Meta:
        model = Bucket
        fields = [
            "id",
            "created_date",
            "modified_date",
            "name",
            "description",
            "transactions",
        ]


class BankAccountSerializer(serializers.ModelSerializer):
    buckets = BucketSerializer(many=True, required=False)
    # transactions = TransactionsSerializer(many=True, required=False)

    class Meta:
        model = BankAccount
        fields = [
            "id",
            "created_date",
            "modified_date",
            "name",
            "description",
            "buckets",
            # "transactions",
        ]


class CategorySerializer(serializers.ModelSerializer):
    transactions = TransactionMiniCategorySerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = [
            "id",
            "created_date",
            "modified_date",
            "name",
            "description",
            "transactions",
        ]