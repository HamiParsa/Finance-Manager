# transactions/views.py
from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum, Count, Q
from datetime import datetime
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['type', 'category', 'payment_method']
    search_fields = ['description']
    ordering_fields = ['date', 'amount']
    ordering = ['-date']
    
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def summary(self, request):
        try:
            user = request.user
            
            total_income = Transaction.objects.filter(
                user=user, 
                type='INCOME'
            ).aggregate(total=Sum('amount'))['total'] or 0
            
            total_expense = Transaction.objects.filter(
                user=user, 
                type='EXPENSE'
            ).aggregate(total=Sum('amount'))['total'] or 0
            
            recent_transactions = Transaction.objects.filter(
                user=user
            ).order_by('-date')[:10]
            
            recent_serializer = TransactionSerializer(recent_transactions, many=True)
            
            return Response({
                'total_income': float(total_income),
                'total_expense': float(total_expense),
                'balance': float(total_income - total_expense),
                'recent_transactions': recent_serializer.data,
                'currency': user.currency,
            })
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def monthly_report(self, request):
        try:
            user = request.user
            year = int(request.query_params.get('year', datetime.now().year))
            month = int(request.query_params.get('month', datetime.now().month))
            
            transactions = Transaction.objects.filter(
                user=user,
                date__year=year,
                date__month=month
            )
            
            category_data = transactions.values('category__name', 'category__icon', 'type').annotate(
                total=Sum('amount'),
                count=Count('id')
            ).order_by('-total')
            
            daily_data = transactions.values('date').annotate(
                income=Sum('amount', filter=Q(type='INCOME')),
                expense=Sum('amount', filter=Q(type='EXPENSE'))
            ).order_by('date')
            
            total_income = transactions.filter(type='INCOME').aggregate(
                total=Sum('amount')
            )['total'] or 0
            
            total_expense = transactions.filter(type='EXPENSE').aggregate(
                total=Sum('amount')
            )['total'] or 0
            
            return Response({
                'year': year,
                'month': month,
                'category_breakdown': list(category_data),
                'daily_summary': list(daily_data),
                'total_income': float(total_income),
                'total_expense': float(total_expense),
            })
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )