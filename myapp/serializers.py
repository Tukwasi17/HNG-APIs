from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    visitor_name = serializers.CharField(max_length=100)
    """location = serializers.CharField(max_length=100)"""