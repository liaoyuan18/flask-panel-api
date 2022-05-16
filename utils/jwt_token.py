import jwt
import datetime
import time
from .json_response import json_resp

SECRET_KEY = "123dffdgdfv"


def generate_token(username: str, user_id: str):
    '''

    :param username:
    :param user_id:
    :return:
    '''
    # 签名
    sign = 'qianming'
    # exp、iat 的时区需要用utc，否则得到的时间戳无法计算是否过期
    dic = {
        'exp': datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=1),  # 设置一天后过期
        'iat': datetime.datetime.now(tz=datetime.timezone.utc),
        'iss': sign,
        'data': {
            'username': username,
            'user_id': user_id
        }
    }
    return jwt.encode(dic, SECRET_KEY, algorithm='HS256')


def verify_token(token):
    '''

    :param token:
    :return: dict ,如果验证失败，返回带有错误代码的字典，否则不带错误代码
    '''
    try:
        d = jwt.decode(token, SECRET_KEY, algorithms='HS256', verify_signature=True, verify_exp=True, verify_iat=True)
        return d
    except jwt.ExpiredSignatureError as e:
        print(e)
        return json_resp(50014)
    except jwt.ImmatureSignatureError as e:
        print(e)
        return json_resp(50008)
