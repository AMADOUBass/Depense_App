from rest_framework import serializers
from .models import Transaction
from django.contrib.auth.models import User

class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Transaction model.
    """
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']
        
  

    def validate(self, attrs):
        if attrs.get('description') and len(attrs['description']) < 5:
            raise serializers.ValidationError("Description must be at least 5 characters long.")
        return attrs



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # include username
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
