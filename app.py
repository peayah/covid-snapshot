from flask import Flask, redirect, render_template, send_file, request
from charts import *

app = Flask(__name__)


def get_monthly_data(country):

    data = search_one_country(country)

    list_of_countries = countries()#[1]
    # data = dict(list_of_countries)
    # return data.get(country, "Data is not found")  # .strip()

    return data


@app.route('/', methods=['GET', 'POST'])
# @app.route('/')
def index():
    """Entry point; the view for the main page"""
    data = []
    if request.method == "POST":
        country = request.form.get('country')
        # return render_template('index.html', data=get_monthly_data(country))
        data = get_monthly_data(country)

    country_data = countries()

    return render_template('index.html',
                           country_data=country_data,
                           data=data)


@app.route('/main.png')
def main_plot():
    """The view for rendering the scatter chart"""
    main_graph = death_cases_graph()

    return send_file(main_graph, mimetype='image/png', cache_timeout=0)


if __name__ == '__main__':
    app.run()
