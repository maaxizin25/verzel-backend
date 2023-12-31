from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data, username=validated_data['email'])


    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data["password"])
        instance.save()
        return instance