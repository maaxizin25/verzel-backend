from rest_framework import serializers
from announcement.models import Announcement, Photos
from django.core.files.storage import FileSystemStorage

class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Announcement
        fields = ['id', 'nome', 'marca', 'model', 'ano', 'valor', 'km', 'placa', 'cor', 'transmissao', 'descricao']
        #extra_kwargs = {'user': {'write_only': True},}

    
