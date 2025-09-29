from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False)
    brand = serializers.CharField(max_length=255)
    price = serializers.IntegerField(default=0)
    made_year = serializers.IntegerField()


#verbose name qoshgandim xatolik berdi ustoz