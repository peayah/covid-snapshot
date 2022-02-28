import matplotlib.pyplot as plt
import data_import
from io import BytesIO
from data_import import return_data_for_one_country


def search_one_country(coun):
    tas=return_data_for_one_country(coun)
    one_country_details = []

    ty_data = tas[0]
    ly_data = tas[1]

    request_data = ty_data.json().get('response')

    # get country name (0)
    this_country = request_data[0]['country']
    one_country_details.append(this_country)

    # get population total (1)
    this_population = request_data[0]['population']
    one_country_details.append(this_population)

    # CASES
    # get  total cases (2)
    this_cases = request_data[0]['cases']['total']
    one_country_details.append(this_cases)

    # get cases today (3)
    if request_data[0]['cases']['new'] is not None:
        todays_cases = int(request_data[0]['cases']['new'].replace("+",""))
    else:
        todays_cases = 0
    one_country_details.append(todays_cases)

    # get last year data
    last_year_request_data = ly_data.json().get('response')

    # get last year's total cases (4)
    last_year_cases = last_year_request_data[0]['cases']['total']
    one_country_details.append(last_year_cases)

    # get the this year and last year case difference (5)
    difference = int(this_cases) - int(last_year_cases)
    one_country_details.append(difference)

    # get cases vs population % (6)
    casespopulation = int(this_cases) / int(this_population) * 100
    one_country_details.append(casespopulation)


    # DEATHS
    # get deaths total (7)
    this_deaths = request_data[0]['deaths']['total']
    one_country_details.append(this_deaths)

    # deaths today (8)
    if request_data[0]['deaths']['new'] is not None:
        today_deaths = int(request_data[0]['deaths']['new'].replace("+",""))
    else:
        today_deaths = 0
    one_country_details.append(today_deaths)

    # get deaths vs population % (9)
    deathpopulation = int(this_deaths) / int(this_population) * 100
    one_country_details.append(deathpopulation)

    # get deaths vs cases % (10)
    deathcases = int(this_deaths) / this_cases * 100
    one_country_details.append(deathcases)

    # get tests total (11)
    this_tests = request_data[0]['tests']['total']
    one_country_details.append(this_tests)

    # average tests per citizens (12)
    test_per_citizen = int(this_tests) / int(this_population)
    one_country_details.append(test_per_citizen)

    # get rise in cases (13)
    rise_in_cases = this_cases / last_year_cases
    one_country_details.append(rise_in_cases)

    return one_country_details


'''
request_data = data_import.one_country_response.json().get('response')

    # get country name (0)
    this_country = request_data[0]['country']
    one_country_details.append(this_country)

    # get population total (1)
    this_population = request_data[0]['population']
    one_country_details.append(this_population)

    # get cases total this year (2)
    this_cases = request_data[0]['cases']['total']
    one_country_details.append(this_cases)

    # get deaths total this year (3)
    this_deaths = request_data[0]['deaths']['total']
    one_country_details.append(this_deaths)

    # get tests total this year (4)
    this_tests = request_data[0]['tests']['total']
    one_country_details.append(this_tests)

    # get cases total this year
    last_year_request_data = data_import.last_year_one_country_response.json().get('response')

    #  get last years cases number (5)
    last_year_cases = last_year_request_data[0]['cases']['total']
    one_country_details.append(last_year_cases)

    # get the difference (6)
    difference = int(this_cases) - int(last_year_cases)
    one_country_details.append(difference)

    # average tests per citizens (7)
    test_per_citizen = int(this_tests) / int(this_population)
    one_country_details.append(test_per_citizen)

    # print(one_country_details)
    return one_country_details


'''


def countries():

    # initialize list
    list_of_countries = []

    for item in data_import.world_response.json().get('response'):
        if item.get('deaths')['new'] is not None:
            if item.get('country') != item.get('continent'):
                new_number = int(item.get('deaths')['new'].replace("+",""))
                list_of_countries.append((item.get('country'), new_number))

    def sort_key(list_of_countries):
        return list_of_countries[1]

    list_of_countries.sort(key=sort_key, reverse=True)

    # print(dict(list_of_countries))
    return list_of_countries


def death_cases_graph():

    # initialize lists
    deaths = []
    cases = []
    tests = []

    # today's data
    for item in data_import.world_response.json().get('response'):

        # if deaths is 0 or more
        if item.get('deaths')['total'] is not None and item.get('population') is not None:
            deaths.append(int(item.get('deaths')['total'])/int(item.get('population'))*100)
        else:
            deaths.append(0)

        # if tests is 0 or more
        if item.get('tests')['total'] is not None and item.get('population') is not None:
            tests.append(int(item.get('tests')['total'])/int(item.get('population')))
        else:
            tests.append(0)

        # if cases is 0 or more
        if item.get('cases')['total'] is not None and item.get('population') is not None:
            cases.append(int(item.get('cases')['total'])/int(item.get('population'))*100)
        else:
            cases.append(0)

    # making  plot
    gridsize = (10, 2)

    plt.figure(figsize=(8, 6))
    now_plt = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=6)
    one_plt = plt.subplot2grid(gridsize, (7, 0), rowspan=3)
    two_plt = plt.subplot2grid(gridsize, (7, 1), rowspan=3)

    # ------------------------
    # main title for plots
    now_plt.set_title('Deaths vs. Cases',
                      fontsize=14)

    # plotting points for now
    # death vs cases scatter plot (x,y)
    now_plt.scatter(deaths,
                    cases,
                    color="darkslategrey",
                    marker=".",
                    s=10)

    # plotting points for one year ago
    # death vs cases scatter plot (x,y)
    one_plt.scatter(tests,
                    cases,
                    color="darkslategrey",
                    marker=".",
                    s=10)
    # death vs cases plot title
    one_plt.set_title('Tests vs. Cases',
                      fontsize=11)

    # plotting points for two yeats ago
    # death vs cases scatter plot (x,y)
    two_plt.scatter(tests,
                    deaths,
                    color="darkslategrey",
                    marker=".",
                    s=10)
    # death vs cases plot title
    two_plt.set_title('Tests vs. Deaths',
                      fontsize=11)

    fig = BytesIO()
    plt.savefig(fig)
    fig.seek(0)
    return fig
