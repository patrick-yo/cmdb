from flask import Blueprint
from flask_restplus import Api
from api.cmdb.compare import ns as compare_api

blueprint = Blueprint('list', __name__, url_prefix='/cmdb', template_folder='templates')

api = Api(blueprint, title='compare', version='1.0', description='1.0')

api.add_namespace(compare_api)


