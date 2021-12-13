from flask import Flask, redirect, url_for, render_template, request, session, send_file
from io import StringIO, BytesIO
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
app.secret_key = "eifuwenff"


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
    # return plt
    plt.savefig(f"images/{country}.png")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/index", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        return render_template("selection.html")
    else:
        return render_template("index.html")


@app.route("/selection", methods=["POST", "GET"])
def selection():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("selection.html")


@app.route('/historical_graphs/<country>')
def images(country):
    app.logger.error(f"{os.getcwd()}/images/{country}.png")
    return render_template("images.html", image=f"{country}.png")


# @app.route('/historical_figure/<country>')
# def fig(country):
#     fig = graph(country)
#     img = BytesIO()
#     fig.savefig(img, format='png')
#     img.seek(0)
#     return send_file(img, mimetype="image/png")


@app.route("/user", methods=["POST", "GET"])
def user():
    if "user" in session:
        user = session["user"]
        # app.logger.error(request.form["history"])
        if "history" in request.form.keys():
            return redirect(f"/historical_graphs/{request.form['nm']}")
        else:
            return "sorry in progress", 200
    else:
        return redirect(url_for("selection"))


if __name__ == '__main__':
    app.run(debug=True, port=6000)
