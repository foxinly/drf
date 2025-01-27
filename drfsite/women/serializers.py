from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Women


class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content



class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()


def encode():
    model = WomenModel('Jolie', 'Angelina Jolie')
    model_sr = WomenSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)