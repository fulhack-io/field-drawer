from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from field_drawer import FieldDrawer
from forms import DrawForm
import simplejson as json
from flask_wtf.csrf import CSRFProtect
from flask_nav import Nav
from flask_nav import register_renderer

from flask_nav.elements import Navbar, View, Link

from dominate import tags
from nav import FDBootstrapRenderer


app = Flask(__name__)
app.secret_key = '€%€%#dfvdgeryj4wi5t4543&342b'
app.config['TEMPLATES_AUTO_RELOAD'] = True
Bootstrap(app)
csrf = CSRFProtect(app)
csrf.init_app(app)

nav = Nav()

@nav.navigation()
def navbar():
    return Navbar(
        'ingress.fulhack.io',
        View('Draw', 'index'),
        Link('Contact', 'contact')

    )
register_renderer(app, 'custom', FDBootstrapRenderer)
nav.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = DrawForm()
    return render_template('draw.html', form=form)


@app.route('/draw', methods=['POST'])
def draw():
    if request.method == 'POST':
        print(request.form)

        parse_anchors = 'parse_anchors' in request.form
        include_markers = 'include_markers' in request.form

        portal_list = request.form['portal_list']
        draw_color = request.form['draw_color']

        if parse_anchors:
            for portal in json.loads(portal_list):
                if portal["type"] == "polyline":
                    anchor1 = '{},{}'.format(portal["latLngs"][0]['lat'], portal["latLngs"][0]['lng'])
                    anchor2 = '{},{}'.format(portal["latLngs"][1]['lat'], portal["latLngs"][1]['lng'])
                    break
        else:
            anchor1 = request.form['anchor1']
            anchor2 = request.form['anchor2']

        field = FieldDrawer(anchor1, anchor2, portal_list, include_markers, draw_color).generate()
        return jsonify(result=field, anchor1=anchor1, anchor2=anchor2)


@app.route('/contact')
def faq():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=8080,
            use_reloader = True,
            threaded=True)
