from rest_framework import serializers
from document import models

class DocumentSerializer(serializers.ModelSerializer):
        class Meta:
                model = models.Document
                fields = '__all__'