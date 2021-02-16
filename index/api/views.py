import json
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import SubscribeSerializer
from ..models import Subscriber
 

class SubscribeView(CreateAPIView):
    serializer_class = SubscribeSerializer
    model = Subscriber