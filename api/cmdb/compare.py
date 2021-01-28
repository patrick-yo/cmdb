from flask import request, render_template
from flask_restplus import Resource, Namespace
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import base64
from io import BytesIO


ns = Namespace('compare', description='cmdb compare')


# venn
# @ns.param('match', 'e.g: 65')
# @ns.param('cmdb', 'e.g: 20')
# @ns.param('caas', 'e.g: 15')
@ns.route('/venn')
# @ns.route('/venn', methods=['GET'])  #传入参数
class Venn(Resource):
    def get(self):

        # caas = request.args.get('caas')
        # cmdb = request.args.get('cmdb')
        # match = request.args.get('match')
        caas, cmdb, match = 15, 20, 65

        my_dpi = 96
        plt.figure(figsize=(480 / my_dpi, 480 / my_dpi), dpi=my_dpi)
        venn2(subsets=(caas, cmdb, match), set_labels=('caas', 'cmdb'))


        sio = BytesIO()
        plt.savefig(sio, format='png')
        data = base64.encodebytes(sio.getvalue()).decode()

        # print(data)
        html = '<html><body><img src="data:image/png;base64,{}" /></body></html>'
        plt.close()

        # return render_template('index.html', data=data)
        # return render_template('index.html')
        return html.format(data)