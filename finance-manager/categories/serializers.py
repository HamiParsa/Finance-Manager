# categories/serializers.py
from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'type', 'icon', 'color', 'is_default', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def validate(self, data):
        user = self.context['request'].user
        if Category.objects.filter(name=data['name'], user=user).exists():
            raise serializers.ValidationError({"name": "Category with this name already exists"})
        return data