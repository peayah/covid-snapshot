import matplotlib.pyplot as plt
import data_import
from io import BytesIO


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
    now_plt = plt.subplot2grid(gridsize, (0,0), colspan=2, rowspan=6)
    one_plt = plt.subplot2grid(gridsize,(7,0), rowspan=3)
    two_plt = plt.subplot2grid(gridsize,(7,1), rowspan=3)

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
