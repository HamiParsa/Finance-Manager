# transactions/serializers.py
from rest_framework import serializers
from .models import Transaction
from categories.models import Category

class TransactionSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_icon = serializers.CharField(source='category.icon', read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'category', 'category_name', 'category_icon', 
                 'amount', 'type', 'description', 'date', 'payment_method', 
                 'receipt', 'is_recurring', 'recurring_period', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def validate(self, data):
        if data.get('category') and data.get('type'):
            category = data['category']
            if category.type != data['type']:
                raise serializers.ValidationError(
                    f"Category type ({category.type}) doesn't match transaction type ({data['type']})"
                )
        return data
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)