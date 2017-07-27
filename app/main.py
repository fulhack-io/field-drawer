from flask import Flask, render_template, request
from field_drawer import FieldDrawer

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def default():
    if request.method == 'POST':
        anchor1 = request.form['anchor1']
        anchor2 = request.form['anchor2']
        portal_list = request.form['portal_list']

        draw_color = request.form['draw_color']

        include_markers = 'include_markers' in request.form

        field = FieldDrawer(anchor1, anchor2, portal_list, include_markers, draw_color).generate()
        return render_template('index.html', field=field)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)
