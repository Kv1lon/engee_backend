from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from obj_ev.models import ObjEv
from obj_ev.serializers import ObjEvProfileSerializer
from users.models import Userc


class UserProfileSerializer(serializers.ModelSerializer):
    """serializer for user's profile"""

    objs = ObjEvProfileSerializer(many=True)

    class Meta:
        model = Userc
        exclude = ('password',)


class UserCreateSerializer(UserCreateSerializer):
    """serializer for creating user*for simple jwt*"""

    pass

    class Meta(UserCreateSerializer.Meta):
        model = Userc
        fields = ("id", "username", "password", "email",)


class UserUpdateSerializer(serializers.ModelSerializer):
    """serializer for updating user"""

    pass

    class Meta:
        model = Userc
        fields = ("email", "id",)
