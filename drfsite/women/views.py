from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from women.models import Women
from women.serializers import WomenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class WomenApiView(APIView):
    def get(self, request):
        ls = Women.objects.all().values()
        return Response({'posts': list(ls)})

    def post(self, request):
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})



# class WomenApiView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer