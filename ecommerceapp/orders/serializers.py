from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    customer = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = '__all__'


    def get_created_by(self, obj):
        return obj.created_by.username if obj.created_by else None

    def get_customer(self, obj):
        return obj.customer.username if obj.customer else None