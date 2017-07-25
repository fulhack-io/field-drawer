# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for
from field_drawer import FieldDrawer

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/', methods=['GET', 'POST'])
def default():
    if request.method == 'POST':
        anchor1=request.form['anchor1']
        anchor2=request.form['anchor2']
        portal_list=request.form['portal_list']

        field = FieldDrawer(anchor1, anchor2, portal_list).generate()
        return render_template('index.html', field=field)
    else:
        return render_template('index.html')

if __name__ == '__main__':
  app.run(
        host="0.0.0.0",
        port=int("8080")
  )
