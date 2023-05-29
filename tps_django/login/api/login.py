# 验证用户名和密码
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from django.contrib.auth import authenticate

class LoginView(APIView): 
    def post(self, request): 
        username = request.data.get('username') 
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # 登录成功，返回用户信息
            return Response({
                'code': 0,
                'message': '登录成功',
                'data': {
                    'username': user.username,
                    'email': user.email,
                    'is_staff': user.is_staff,
                    'is_superuser': user.is_superuser
                }
            })
        else:
            # 登录失败，返回错误信息
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({
                    'code': -1,
                    'message': '用户名或密码错误'
                }, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({
                    'code': -1,
                    'message': '用户名或密码错误'
                }, status=status.HTTP_401_UNAUTHORIZED)