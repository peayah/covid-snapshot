from flask import Flask, render_template, send_file

import charts
from charts import *
import data_import

app = Flask(__name__)


@app.route('/')
def index():
    """Entry point; the view for the main page"""
    data = countries()
    # for key, val in data:
    #     print(key, val)
    #
    cities = data

    # return render_template('index.html')
    return render_template('index.html', cities = cities)


@app.route('/main.png')
def main_plot():
    """The view for rendering the scatter chart"""
    main_graph = death_cases_graph()

    return send_file(main_graph, mimetype='image/png', cache_timeout=0)


if __name__ == '__main__':
    app.run()
