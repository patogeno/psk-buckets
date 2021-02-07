# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (
    TransactionSerializer,
    BucketSerializer,
    BankAccountSerializer,
    CategorySerializer,
)
from .models import Bucket, BankAccount, Category, Transaction
from django_filters import rest_framework as filters

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ["bucket"]
