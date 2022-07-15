from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from stats.serializers import StatSerializer
from stats.models import Stat
from .models import ObjEv



class ObjEvProfileSerializer(serializers.ModelSerializer):
    """serializer for country's profile"""
    stat_domen = serializers.SerializerMethodField()

    class Meta:
        model = ObjEv
        fields = ("title",  "slug",  "id","stat_domen","alarm")

    def get_stat_domen(self, instance):
        stats = instance.stat_domen.all().order_by('-date')
        return StatSerializer(stats, many=True).data


class ObjEvCreateSerializer(serializers.ModelSerializer):
    """serializer for creating post"""


    class Meta:
        model = ObjEv
        fields = ("title",)
