from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
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

    def list(self, request, *args, **kwargs):
        ''' Modify list query to sort by datetime field descending
        '''
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        serializer_data = sorted(
            serializer.data, key=lambda k: k["datetime"], reverse=True
        )
        return Response(serializer_data)
