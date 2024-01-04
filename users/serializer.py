from rest_framework import serializers
from users.models import User
from announcement.models import Announcement

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model =Announcement
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    announcements = AnnouncementSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'announcements']
        
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data, username=validated_data['email'])


    def update(self, instance, validated_data):
        for field_name, value in validated_data.items():
            setattr(instance, field_name, value)
        if 'password' in validated_data:
            instance.set_password(validated_data["password"])
        instance.save()
        return instance
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        announcements = AnnouncementSerializer(Announcement.objects.filter(user=instance), many=True).data
        data['announcements'] = announcements
        return data