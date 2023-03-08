from rest_framework import serializers


class WishListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    
    class Meta:
        fields = ['id']