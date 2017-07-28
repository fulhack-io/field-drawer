from flask import Flask, render_template, request
from field_drawer import FieldDrawer
import simplejson as json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def default():
    if request.method == 'POST':

        parse_anchor = 'parse_anchor' in request.form
        include_markers = 'include_markers' in request.form

        portal_list = request.form['portal_list']
        draw_color = request.form['draw_color']

        if parse_anchor:
            for portal in json.loads(portal_list):
                if portal["type"] == "polyline":
                    anchor1 = '{},{}'.format(portal["latLngs"][0]['lat'], portal["latLngs"][0]['lng'])
                    anchor2 = '{},{}'.format(portal["latLngs"][1]['lat'], portal["latLngs"][1]['lng'])
                    break
        else:
            anchor1 = request.form['anchor1']
            anchor2 = request.form['anchor2']

        field = FieldDrawer(anchor1, anchor2, portal_list, include_markers, draw_color).generate()
        return render_template('index.html', anchor1=anchor1, anchor2=anchor2, field=field)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
