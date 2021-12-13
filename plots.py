import pandas as pd
import matplotlib.pyplot as plt


def add_country_lower(data):
    country_names = data["Country Name"].values
    country_names = [name.lower() for name in country_names]
    data["country_lower"] = country_names
    # return data


def graph(country):
    file_path = 'CO2_Emissions_1960-2018.csv'
    df_co2 = pd.read_csv(file_path)

    add_country_lower(df_co2)

    df_co2 = df_co2.dropna()

    fig, ax = plt.subplots(1, 1)

    df_US = df_co2[df_co2["country_lower"] == country.lower()]  # row where country name is united states
    year = 1959
    year_list = []
    emissions = []
    while year != 2018:
        year += 1
        year_list.append(year)
        emission_stat = df_US[str(year)]
        emissions.append(emission_stat.values)

    plt.plot(year_list, emissions)
    ax.set(xlabel="Year", ylabel="Emissions (metric ton/capita)", title=country)
    return plt



