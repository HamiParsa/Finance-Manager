# budgets/serializers.py
from rest_framework import serializers
from .models import Budget

class BudgetSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Budget
        fields = ['id', 'user', 'category', 'category_name', 'amount', 'period', 'month', 'year', 'created_at']
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {
            'user': {'read_only': True}
        }
    
    def validate(self, data):
        user = self.context['request'].user
        if Budget.objects.filter(
            user=user, 
            category=data['category'], 
            month=data['month'], 
            year=data['year']
        ).exists():
            raise serializers.ValidationError(
                "Budget for this category and month already exists"
            )
        return data