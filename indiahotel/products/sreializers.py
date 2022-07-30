from rest_framework import serializers
class ProdcutSerializer(serializers.Serializer):
    name=serializers.CharField()
    spec=serializers.CharField()
    price=serializers.IntegerField()