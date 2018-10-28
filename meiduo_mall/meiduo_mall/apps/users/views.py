from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.serializers import UserSerializer


#  GET usernames/(?P<username>\w{5,20})/count/
class UsernameCountView(APIView):
    """判断用户是否存在"""
    def get(self, request, username):
        # 查询数据库匹配用户名,用户数量
        count = User.objects.filter(username=username).count()
        data = {
            'username': username,
            'count': count
        }
        return Response(data)


# GET mobiles/(?P<mobile>1[3-9]\d{9})/count
class MobileCountView(APIView):
    """判断手机号是否存在"""
    def get(self, request, mobile):

        count = mobile = User.objects.filter(mobile=mobile)
        data = {
            'mobile': mobile,
            'count': count
        }
        return Response(data)


# # url(r'^users/$', views.UserView.as_view()),
class UserView(GenericAPIView):
    # 注册用户信息的保存:
    #     1. 接收参数并进行校验(参数完整性，两次密码是否一致，，短信验证码是否正确，)
    #     2. 创建新用户并保存注册用户的信息
    #     3. 返回应答，注册成功

    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        # 接收参数并进行校验
        serializer.is_valid(raise_exception=True)
        # 创建新用户并保存注册用户的信息
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
