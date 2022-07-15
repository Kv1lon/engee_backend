
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import ObjEv
from .serializers import ObjEvProfileSerializer, ObjEvCreateSerializer
from users.models import Userc
from slugify import slugify


class ProfileObjEv(RetrieveAPIView):
    """view of country`s profile"""
    serializer_class = ObjEvProfileSerializer
    queryset = ObjEv.objects.all()
    lookup_field = "slug"


class ObjEvDetail(ListAPIView):
    """view of country`s profile"""
    serializer_class = ObjEvProfileSerializer
    queryset = ObjEv.objects.filter()
    pagination_class = None


    def get_queryset(self):
        user = Userc.objects.get(username = self.request.user.username)
        return user.objs
class ObjEvCreate(CreateAPIView):
    """view for creating article"""
    serializer_class = ObjEvCreateSerializer



