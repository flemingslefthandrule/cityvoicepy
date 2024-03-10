from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'aadhar', 'is_expert', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['aadhar'],
            validated_data['password'],
            is_expert=validated_data.get('is_expert', False)
        )
        return user