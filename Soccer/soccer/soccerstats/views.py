from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics, mixins
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import *
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.authentication import BasicAuthentication


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


# Create your views here.
class MatchListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    queryset            = Match.objects.all()
    serializer_class    = MatchListSerializer
    permission_classes = [IsAuthenticated|ReadOnly]

    def get_queryset(self):
        query = Match.objects.all()
        return query

    def post(self,request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        serialized_data = MatchListSerializer(data=request.data, many=is_many)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=201)
        else:
            return Response(serialized_data.errors, status=400)


class MatchAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    queryset            = Match.objects.all()
    serializer_class    = MatchSerializer
    lookup_field        = 'id'
    permission_classes = [IsAuthenticated|ReadOnly]
    authentication_classes = [BasicAuthentication]


    def put(self, request, *args, **kwargs):
        query = Match.objects.get(id=self.kwargs['id'])
        serialized_data = MatchSerializer(query, data=request.data, partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=200)
        else:
            return Response(serialized_data.errors, status=400)

    def delete(self, request, *args, **kwargs):
        qs = Match.objects.get(id=self.kwargs['id'])
        if qs is not None:
            qs.delete()
            return Response(status=204)
        else:
            return Response({"detail": "Wybrany mecz nie istnieje, bądź wystąpił błąd po stronie serwera."},status=400) 
        

class TeamListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamListSerializer
    permission_classes = [IsAuthenticated|ReadOnly]
    authentication_classes = [BasicAuthentication]

    def get_queryset(self):
        query = Team.objects.all()
        return query

    def post(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        serialized_data = TeamListSerializer(data=request.data, many=is_many)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=201)
        else:
            return Response(serialized_data.errors, status=400)

class TeamAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = ['id']
    permission_classes = [IsAuthenticated|ReadOnly]
    authentication_classes = [BasicAuthentication]

    def get(self, *args, **kwargs):
        query = Team.objects.get(id=self.kwargs['id'])
        serialized_data = TeamSerializer(query)
        return Response(serialized_data.data, status=200)

    def put(self, request, *args, **kwargs):
        query = Match.objects.get(id=self.kwargs['id'])
        serialized_data = MatchSerializer(query, data=request.data, partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=200)
        else:
            return Response(serialized_data.errors, status=400)

    def delete(self, request, *args, **kwargs):
        qs = Team.objects.get(id=self.kwargs['id'])
        if qs is not None:
            qs.delete()
            return Response(status=204)
        else:
            return Response({"detail": "Wybrana drużyna nie istnieje, bądź wystąpił błąd po stronie serwera."},status=400) 

class PlayerListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated|ReadOnly]
    authentication_classes = [BasicAuthentication]

    def get_queryset(self):
        query = Player.objects.all()
        return query

    def post(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        serialized_data = PlayerSerializer(data=request.data, many=is_many)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=201)
        else:
            return Response(serialized_data.errors, status=400)

class PlayerAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = ['id']
    permission_classes = [IsAuthenticated|ReadOnly]
    authentication_classes = [BasicAuthentication]

    def get(self, *args, **kwargs):
        query = Player.objects.get(id=self.kwargs['id'])
        serialized_data = PlayerSerializer(query)
        return Response(serialized_data.data, status=200)

    def put(self, request, *args, **kwargs):
        query = Player.objects.get(id=self.kwargs['id'])
        serialized_data = PlayerSerializer(query, data=request.data, partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=200)
        else:
            return Response(serialized_data.errors, status=400)

    def delete(self, request, *args, **kwargs):
        qs = Player.objects.get(id=self.kwargs['id'])
        if qs is not None:
            qs.delete()
            return Response(status=204)
        else:
            return Response({"detail": "Wybrana drużyna nie istnieje, bądź wystąpił błąd po stronie serwera."},status=400) 

class MatchShotsListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = ShotSerializer
    permission_classes = [IsAuthenticated|ReadOnly]
    authentication_classes = [BasicAuthentication]

    def get_queryset(self):
        query = Shot.objects.filter(match__id = self.kwargs['id'])
        return query

    def post(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        serialized_data = ShotSerializer(data=request.data, many=is_many)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=201)
        else:
            return Response(serialized_data.errors, status=400)

class MatchPassesListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = PassSerializer
    permission_classes = [IsAuthenticated|ReadOnly]
    authentication_classes = [BasicAuthentication]

    def get_queryset(self):
        query = Pass.objects.filter(match__id = self.kwargs['id'])
        return query

    def post(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        serialized_data = PassSerializer(data=request.data, many=is_many)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=201)
        else:
            return Response(serialized_data.errors, status=400)