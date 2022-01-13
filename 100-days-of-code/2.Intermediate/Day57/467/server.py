from flask import Flask, render_template
import requests

app = Flask(__name__)

parameter = {
    "name": "Angela"
}

response = requests.get("https://api.genderize.io", params=parameter).json()
print(response)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/test/<name>")
def guess(name):
    parameter = {
        "name": name
    }
    gender_response = requests.get(url="https://api.genderize.io", params=parameter).json()
    gender = gender_response["gender"]
    age_response = requests.get(url="https://api.agify.io", params=parameter).json()
    age = age_response["age"]
    return render_template("guess.html", first_name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)