from rest_framework import serializers

from folder_view.folder_view.models import Prefix, Word

class PrefixSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prefix
        fields = ["name"]

class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ["word", "prefix"]
