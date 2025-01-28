from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home(): 
    info = {}
    random_number = random.randint(1, 10)
    name = "Jayasurya Marasani"
    date = datetime.date.today().year 
    info["num"] = random_number
    info["name"] = name
    info["year"] = date

    return render_template("index.html",info=info)


@app.route("/guess/<name>")
def guess(name):
    info = {"name" : name.title()}
    parameters = {
        "name" : name,
    }
    response = requests.get(url="https://api.agify.io", params = parameters)
    response.raise_for_status()
    text = response.json()
    info["age"] = text["age"]
    response = requests.get(url="https://api.genderize.io", params=parameters)
    response.raise_for_status()
    text = response.json()
    info["gender"] = text["gender"]
    return render_template("guess.html", info = info)

@app.route("/blog")
def get_blog():
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    data = response.json()

    return render_template("blog.html", posts = data)

if __name__ == "__main__":
    app.run(debug=True)