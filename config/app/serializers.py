from rest_framework import serializers
from .models import Cars, Driver


class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False)
    brand = serializers.CharField(max_length=255)
    price = serializers.IntegerField(default=0)
    made_year = serializers.IntegerField()
    category = serializers.SerializerMethodField()   # ForeignKey ni toza chiqarish uchun

    def get_category(self, obj):
        return obj.category.id   # Kaategoriyasini ham chiqarih uchun !!

    def create(self, validated_data):
        return Cars.objects.create(**validated_data)


class DriverSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    age = serializers.IntegerField(default=18)
    experience_years = serializers.IntegerField(default=0)

    def create(self, validated_data):
        return Driver.objects.create(**validated_data)
