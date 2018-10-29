from django.shortcuts import render

# Create your views here.

# API: GET /oauth/qq/authorization/?next=<登录成功跳转页面地址>
from rest_framework.views import APIView


class QQAuthView(APIView):

    def get(self, request):
        # """ 获取QQ登录网址:
        # 1. 获取next
        # 2. 组织QQ登录网址和参数
        # 3. 返回QQ登录网址
        # """
        #
        # next = request.get_params.get('next')
        pass
