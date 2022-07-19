import requests
from django.shortcuts import redirect
from django.views import View
from msrest.exceptions import ValidationError
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, get_object_or_404, ListAPIView, CreateAPIView, \
    DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

from .models import Userc
from .serializers import UserProfileSerializer, UserUpdateSerializer
from obj_ev.models import ObjEv


class Profile(RetrieveAPIView):
    """view of user`s profile"""
    serializer_class = UserProfileSerializer
    queryset = Userc.objects.all()
    lookup_field = 'slug'


class ProfileUpdate(UpdateAPIView):
    """view for updating profile"""
    serializer_class = UserUpdateSerializer
    queryset = Userc.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def update(self, request, *args, **kwargs):
        username = self.request.user.id
        if int(username) != int(self.get_object().id):
            return Response({'success': False, 'message': "Can't delete this"}, status=status.HTTP_400_BAD_REQUEST)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class UserActivationView(View):

    def get(self, request, uid, token, format=None):
        response = redirect('https://engee.herokuapp.com/users/activation/' + uid + '/' + token)
        return response


class ResetPasswordView(View):
    def get(self, request, uid, token, format=None):
        response = redirect('https://engee.herokuapp.com/users/reset_password/' + uid + '/' + token)
        return response


class AddObj(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, slug):
        user = get_object_or_404(Userc.objects.all(), slug=slug)
        print(request.data)
        user.objs.add(ObjEv.objects.get(title=request.data.get('title')))
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RemoveObj(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, slug):
        user = get_object_or_404(Userc.objects.all(), slug=slug)
        print(request.data)
        user.objs.remove(ObjEv.objects.get(title=request.data.get('title')).id)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
