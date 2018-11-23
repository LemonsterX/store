from rest_framework import serializers
from areas.models import Area


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'name')


class SubAreaSerializer(serializers.ModelSerializer):
    # subs = serializers.StringRelatedField(many=True)
    subs = AreaSerializer(label='下级地区', many=True)

    class Meta:
        model = Area
        fields = ('id', 'name', 'subs')
