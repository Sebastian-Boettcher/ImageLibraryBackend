from rest_framework import serializers

class Files(object):
    def __init__(self,image):
        self.image = image

class FileSerializer(serializers.Serializer):
    image = serializers.ImageField()

