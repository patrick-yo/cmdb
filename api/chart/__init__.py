from flask import Blueprint

chart_blue = Blueprint('user', __name__, template_folder='templates', url_prefix='/chart')

from api.chart import venn