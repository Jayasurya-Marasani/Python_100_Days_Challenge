from flask import Flask, render_template
import random
import datetime

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

if __name__ == "__main__":
    app.run(debug=True)