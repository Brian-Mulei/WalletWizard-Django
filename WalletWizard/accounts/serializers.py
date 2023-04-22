from .models import Account
from rest_framework import serializers
from django.contrib.auth.models import User


class AccountSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), read_only=True)

    class Meta:
        model = Account
        fields = '__all__'