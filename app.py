from flask import Flask,jsonify
from packages import system_tool
app = Flask(__name__)


@app.route('/api/system')
def system_info():
    data=system_tool.system_info()
    return jsonify(data)

if __name__ == '__main__':
    app.run()
