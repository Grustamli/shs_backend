from ..serializers.ads import (AdListSerializer, AdCreateSerializer, AdDetailSerializer)
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404


from ..models.ads import Ad
from ..models.user import Person
from ..models.add_on import AppliedAddOn
from rest_framework.parsers import JSONParser

class AdListView(APIView):
    def get(self, request, format=None):
        queryset = Ad.objects.all()
        serializer = AdListSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = AdCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = self.request.user
            person = Person.objects.get(id=user.id)
            serializer.save(person=person)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AdDetailView(APIView):
    def get_object(self, pk):
        try:
            return Ad.objects.get(pk=pk)
        except Ad.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print(self.get_object(pk))
        ad = self.get_object(pk)
        ad = AdDetailSerializer(ad)
        return Response(ad.data)


    def delete(self, request, pk, format=None):
        ad = self.get_object(pk)
        print(ad)
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
