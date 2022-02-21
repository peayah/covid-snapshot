from flask import Flask, render_template, send_file
from charts import *

app = Flask(__name__)


@app.route('/')
def index():
    """Entry point; the view for the main page"""
    country_data = countries()

    # return render_template('index.html')
    return render_template('index.html', country_data = country_data)


@app.route('/main.png')
def main_plot():
    """The view for rendering the scatter chart"""
    main_graph = death_cases_graph()

    return send_file(main_graph, mimetype='image/png', cache_timeout=0)


if __name__ == '__main__':
    app.run()
