from random import random
from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
# import random
from . import constants


class SMSCodeView(APIView):
    # """短信验证码"""
    #
    # def get(self, request, mobile):
    #     """发送短信验证码"""
    #     # 判断图片验证码,判断是否在60s内
    #     redis_conn = cache()
    #     send_flag = redis_conn.get("send_flag_%s" % mobile)
    #     if send_flag:
    #         return Response({"message": '请求次数过于频繁'}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     # 生成短信验证码
    #     sms_code = "%06d" % random.randint(0, 999999)
    #
    #     # 保存短信验证码与发送记录
    #     redis_conn = get_redis_connection('verify_codes')
    #     pl = redis_conn.pipeline()
    #     pl.setex("sms_%s" % mobile, constants.SMS_CODE_REDIS_EXPIRES, sms_code)
    #     pl.setex('send_flag_%s' % mobile, constants.SEND_SMS_CODE_INTERVAL, 1)
    #     pl.execute()
    #
    #     # 发送短信验证码
    #     sms_code_expires = constants.SMS_CODE_REDIS_EXPIRES // 60
    #     try:
    #         ccp = CCP()
    #         res = ccp.send_template_sms(mobile, [code, expires], SMS_CODE_TEMP_ID)
    #     except Exception as e:
        pass
