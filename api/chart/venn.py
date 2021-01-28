from api.chart import chart_blue
from flask import render_template, request
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import base64
from io import BytesIO


# 与cmdb的集合图
def venn(name, left, right, cross):
    my_dpi = 96
    plt.figure(figsize=(480/my_dpi, 480/my_dpi), dpi=my_dpi)
    venn2(subsets=(left, right, cross), set_labels=(name, 'cmdb'))
    return plt

# 转码展示
def transcode(fig):
    sio = BytesIO()
    fig.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    return data


@chart_blue.route('/venn/<name>')
def show_venn(name):
    ratio1 = float(request.args.get('ratio1'))
    ratio2 = float(request.args.get('ratio2'))
    match = float(request.args.get('match'))
    fig = venn(name, ratio1, ratio2, match)
    data = transcode(fig)
    fig.close()
    return render_template('index.html', data=data)