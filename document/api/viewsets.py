from rest_framework import viewsets
from document.api import serializers
from document import models

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer
