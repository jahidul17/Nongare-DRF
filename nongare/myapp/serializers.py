from rest_framework import serializers
from .models import Snippet

# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Snippet
#         fields=['name','title','description']



#when use Relation and Hiperlink condition
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Snippet
        fields=['url','owner','name','title','description']

