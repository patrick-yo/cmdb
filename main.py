from flask import Flask
from api.chart import chart_blue
# from api.cmdb import blueprint as cmdb_blue

__author__ = 'yan'

app = Flask(__name__)


# 注册蓝图
app.register_blueprint(chart_blue)
# app.register_blueprint(cmdb_blue)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )
