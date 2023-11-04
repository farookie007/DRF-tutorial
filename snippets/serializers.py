from rest_framework import serializers

from accounts.models import CustomUser
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES



class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(view_name="snippet-highlight", format="html")


    class Meta:
        model = Snippet
        fields = ["url", "id", "highlight", "title", "code", "owner", "linenos", "language", "style"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(view_name="snippet-detail", many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ["url", "id", "username", "snippets"]
