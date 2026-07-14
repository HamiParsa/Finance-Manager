# budgets/views.py
from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum
from datetime import datetime
from .models import Budget
from .serializers import BudgetSerializer
from transactions.models import Transaction  

class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['category', 'period', 'month', 'year']
    ordering_fields = ['amount', 'month', 'year']
    
    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def current_month(self, request):
        user = request.user
        now = datetime.now()
        budgets = Budget.objects.filter(
            user=user,
            month=now.month,
            year=now.year
        )
        serializer = BudgetSerializer(budgets, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def progress(self, request):
        user = request.user
        now = datetime.now()
        
        budgets = Budget.objects.filter(
            user=user,
            month=now.month,
            year=now.year
        ).select_related('category')
        
        result = []
        for budget in budgets:
            spent = Transaction.objects.filter(
                user=user,
                category=budget.category,
                type='EXPENSE',
                date__month=now.month,
                date__year=now.year
            ).aggregate(Sum('amount'))['amount__sum'] or 0
            
            result.append({
                'budget': BudgetSerializer(budget).data,
                'spent': spent,
                'remaining': budget.amount - spent,
                'percentage': (spent / budget.amount * 100) if budget.amount > 0 else 0
            })
        
        return Response(result)