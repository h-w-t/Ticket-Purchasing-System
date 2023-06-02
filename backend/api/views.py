from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import View
from .serializers import UserSerializer

class LoginView(View):
  def post(self, request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      # 验证成功,返回响应
      return Response(serializer.data)
    return Response(serializer.errors, status=400)