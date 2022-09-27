import imp
from rest_framework import serializers
from .models import UserProfile, Order, Ingredient, CustomerDetail

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UserProfile
        fields = ('id', 'email', 'password')

        extra_kwargs = {
        'password': {
            'write_only': True,
            'style': {'input_type': 'password'}
        }}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        exclude = ['id']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
        exclude = ['id']

class OrderSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer()
    customer = CustomerSerializer()
    class Meta:
        model = Order
        fields = '__all__'

