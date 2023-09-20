from rest_framework.serializers import ModelSerializer
from .models import NewsModel
class NewsSerializer(ModelSerializer):
    class Meta:
        model=NewsModel
        fields=('__all__')
