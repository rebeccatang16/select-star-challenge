from django.shortcuts import render
from rest_framework import viewsets, permissions
from folder_view.folder_view.serializers import PrefixSerializer, WordSerializer
from folder_view.folder_view.models import Prefix, Word

class PrefixViewSet(viewsets.ModelViewSet):
    queryset = Prefix.objects.all()
    serializer_class = PrefixSerializer
    permission_classes = [permissions.IsAuthenticated]

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [permissions.IsAuthenticated]