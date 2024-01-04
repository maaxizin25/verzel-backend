from rest_framework import serializers
from announcement.models import Announcement, Photos
from users.models import User
from django.core.files.storage import FileSystemStorage
import cloudinary.uploader

class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ['id', 'image']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']



class AnnouncementSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    photos = PhotosSerializer(many=True, read_only=True)

    class Meta:
        model = Announcement
        fields = ['id', 'nome', 'marca', 'model', 'ano', 'valor', 'km', 'placa', 'cor', 'transmissao', 'descricao', 'user', 'photos']
        extra_kwargs = {'user': {'write_only': True},}
    
    def create(self, validated_data):
        user = validated_data.pop('user')
        announcement = Announcement.objects.create(user=user, **validated_data)

        images_data = self.context['request'].FILES.getlist('image')

        if images_data:
            for image_data in images_data:
                upload_result = cloudinary.uploader.upload(image_data)
                image_url = upload_result.get('url')

                Photos.objects.create(anuncio = announcement, image=image_url)

        return announcement
    
    def validate(self, data):
        request = self.context.get('request')
        if request and request.method == "PATCH":
            return data

        images_data = self.initial_data.getlist('image')
        if not images_data:
            raise serializers.ValidationError("É necessário fornecer pelo menos uma imagem.")

        return data
    
    def update(self, instance, validated_data):
        images_data = self.context['request'].FILES.getlist('image')
        if images_data:
            for image_data in images_data:
                upload_result = cloudinary.uploader.upload(image_data)
                image_url = upload_result.get('url')
                Photos.objects.create(anuncio = instance, image=image_url)
        for field_name, value in validated_data.items():
            setattr(instance, field_name, value)
        return instance
    

    