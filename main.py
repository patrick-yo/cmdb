from flask import Flask
from api.chart import chart_blue

__author__ = 'yan'

app = Flask(__name__)

app.register_blueprint(chart_blue)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )
