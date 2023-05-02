from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'user', 'account', 'category', 'amount', 'description', 'created_at')
        read_only_fields = ('created_at',)

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        return Transaction.objects.create(user=user, **validated_data)