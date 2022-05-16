from flask import jsonify


def json_resp(status_code, res_data=None, message=None):
    '''

    :param status_code:
    :param data:
    :param message:
    :return:
    '''
    status = {
        "50008": "illegal token",
        "20000": "sucess",
        "50014":"token has expired"
    }

    if message == None:
        message = status.get(str(status_code), "unkonwn")

    return jsonify({"code": status_code, "data": res_data, "message": message})
