from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.exceptions import ValidationError

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, \
    get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

from obj_ev.views import ObjEv
from users.models import Userc
from .models import Stat
from .serializers import StatListSerializer, StatSerializer, StatCreateSerializer
from slugify import slugify
from datetime import date
from django.core.mail import send_mail

from frag.settings import EMAIL_HOST_USER


class StatCreate(APIView):
    """view for creating article"""
    def get(self,request, format = None):
        serializer = StatCreateSerializer(data= request.query_params)
        serializer.is_valid()
        validated_data = serializer.validated_data
        try:
            ObjEv.objects.get(title=validated_data.get('domen',None))
        except ObjEv.DoesNotExist:
            ObjEv.objects.create(
                title=validated_data.get('domen',None),)
        try:
            Stat.objects.get(slug=slugify(str(date.today().strftime("%d-%m-%Y-%H-%M-%S"))))
        except Stat.DoesNotExist:
            stat = Stat.objects.create(
                Uin=validated_data.get('Uin', None),
                Uout=validated_data.get('Uout', None),
                temp=validated_data.get('temp', None),
                voltage=validated_data.get('voltage', None),
                domen = ObjEv.objects.get(title = validated_data.get('domen', None)),
                slug = slugify(str(date.today().strftime("%d-%m-%Y-%H-%M-%S")))
                )
            stat.save()
            if (ObjEv.objects.get(title=validated_data.get('domen', None)).alarm ==False) & ((int(validated_data.get('Uin', None))!=1) | (int(validated_data.get('Uout', None))!=1)| (int(validated_data.get('temp', None))>162)| (int(validated_data.get('voltage', None))>2.5)):
                obj= ObjEv.objects.get(title=validated_data.get('domen', None))
                obj.alarm = True
                obj.save()
                for user in ObjEv.objects.get(title=validated_data.get('domen', None)).users_domen.all():

                    send_mail("АВАРИЯ",
                              "Показания:Uin="+validated_data.get('Uin', None)+
                              ",Uout="+validated_data.get('Uout', None)+
                              ",temp="+validated_data.get('temp', None)+
                              ",voltage="+validated_data.get('voltage', None),
                              EMAIL_HOST_USER, [user.email], fail_silently=False)
            elif (ObjEv.objects.get(title=validated_data.get('domen', None)).alarm ==True) & ((int(validated_data.get('Uin', None))==1) | (int(validated_data.get('Uout', None))==1)
                | (int(validated_data.get('temp', None))<162)| (int(validated_data.get('voltage', None))<2.5)):
                print(111)
                obj= ObjEv.objects.get(title=validated_data.get('domen', None))
                obj.alarm = True
                obj.save()
                for user in ObjEv.objects.get(title=validated_data.get('domen', None)).users_domen.all():
                    send_mail("авария устранена",
                              "Показания:Uin="+validated_data.get('Uin', None)+
                              ",Uout="+validated_data.get('Uout', None)+
                              ",temp="+validated_data.get('temp', None)+
                              ",voltage="+validated_data.get('voltage', None),
                              EMAIL_HOST_USER, [user.email], fail_silently=False)
        return Response(serializer.data)



class StatDelete(DestroyAPIView):
    """view for deleting article"""
    serializer_class = StatSerializer
    queryset = Stat.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):

        username = self.request.user.email
        if str(self.get_object().author) != str(username):
            return Response({'success': False, 'message': "Can't delete this"}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(self.get_object())
        return Response({'success': True, 'message': "Deleted"}, status=status.HTTP_204_NO_CONTENT)


class StatList(ListAPIView):
    """view of list of posts"""
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return Stat.objects.all().order_by('-date')

    serializer_class = StatListSerializer


class StatDetail(RetrieveAPIView):
    """view of blog`s detail"""
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    lookup_field = "slug"

