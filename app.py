from flask import Flask, jsonify, request, session, redirect, current_app
from flask_httpauth import HTTPBasicAuth
from packages import system_tool
from flask_cors import CORS
from sqlalchemy.orm import Session
from models import User, engine
from utils.jwt_token import generate_token, verify_token
from utils.json_response import json_resp

app = Flask(__name__)
CORS(app, supports_credentials=True)
# app.secret_key = '123123123'
auth = HTTPBasicAuth()


@app.route('/api/login/', methods=['GET', 'POST'])
# @auth.login_required
def login():
    user = request.json
    print(user)
    # 验证user是否正确
    with Session(engine) as session:
        user_d = session.query(User).filter_by(name=user['username']).first()
        if not user_d:
            return jsonify({"code": 20001, "message": "账号或者密码错误"})
        elif user_d.password != user['password']:
            return jsonify({"code": 20001, "message": "账号或者密码错误"})
        else:
            token = generate_token(user_d.name, user_d.user_id)
            resp = jsonify({"token": token, 'code': 20000})
            resp.set_cookie('token', token)
            return resp


@app.route('/api/user_info/', methods=['GET'])
def user_info():
    # 验证token，如果验证失败直接返回
    args = request.args
    token = args.get('token', '')
    data = verify_token(token)
    if data.get("code"):
        return data
    else:
        with Session(engine)as session:
            user = session.query(User).filter_by(user_id=data['data']['user_id']).first()
            return jsonify({"code": 20000, "user_info": user.to_json()})


@app.route('/')
def hello():
    return '123'


@app.route('/api/system/')
def system_info():
    h = request.headers['X-Token']
    if verify_token(h):
        data = system_tool.system_info()
        return json_resp(20000, data)
    else:
        return json_resp(50008)


@app.route('/api/memory/')
def system_memory():
    h = request.headers['X-Token']
    if verify_token(h):
        data = system_tool.ram_info()
        return json_resp(20000, data)
    else:
        return json_resp(50008)


if __name__ == '__main__':
    app.run()
