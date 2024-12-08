from flask import Flask,render_template,request
from predict import MyModel

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",gold = -1,silver = -1,bronze = -1)

@app.route('/submit', methods=['POST'])
def submit():
    country = request.form.get("countries")
    if country == "Select a country":
        return render_template("index.html",gold = -1,silver = -1,bronze = -1)
    else:
        model = MyModel()
        gold = model.predictMedals(model.getMedals("data/GoldMedals.xlsx", country))
        silver = model.predictMedals(model.getMedals("data/SilverMedals.xlsx", country))
        bronze = model.predictMedals(model.getMedals("data/BronzeMedals.xlsx", country))
        return render_template("index.html", gold=gold, silver=silver, bronze=bronze)