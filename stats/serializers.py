from rest_framework import serializers

from obj_ev.models import ObjEv
from .models import Stat


class StatListSerializer(serializers.ModelSerializer):
    """serializer for list of posts"""

    domen = serializers.SlugRelatedField(slug_field='slug', read_only=True)
    date = serializers.DateTimeField(format = "%Y-%m-%d%H:%M:%S")

    class Meta:
        model = Stat
        fields = ("date", "domen", "id", "slug", "Uin", "Uot", "temp", "voltage")


class StatSerializer(serializers.ModelSerializer):
    """serializer for single post"""

    domen = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    date = serializers.DateTimeField(required=False,format = "%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Stat
        fields = "__all__"


class StatCreateSerializer(serializers.ModelSerializer):
    """serializer for creating post"""

    domen = serializers.CharField(write_only=True)

    def create(self, validated_data):
        try:
            ObjEv.objects.get(title=validated_data.get('domen', None))
        except ObjEv.DoesNotExist:
            ObjEv.objects.create(
                title=validated_data.get('domen', None),)

        stat = Stat.objects.create(
            Uin=validated_data.get('Uin', None),
            Uout=validated_data.get('Uout', None),
            temp=validated_data.get('temp', None),
            voltage=validated_data.get('voltage', None),
            domen = ObjEv.objects.get(title = validated_data.get('domen', None))
            )
        stat.save()
        return stat

    class Meta:
        model = Stat
        fields = "__all__"
