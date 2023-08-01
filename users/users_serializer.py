from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

USER_MODEL = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_repeat = serializers.CharField(write_only=True)

    class Meta:
        model = USER_MODEL
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_repeat']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, data):
        validate_password(data)
        return data

    def validate_password_repeat(self, data):
        if data != self.initial_data.get('password'):
            raise serializers.ValidationError('Passwords should be match! Check your passwords')
        return data

    def create(self, validated_data):
        del validated_data['password_repeat']
        user = USER_MODEL.objects.create(**validated_data)
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = ('username', 'password')


class UserRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
