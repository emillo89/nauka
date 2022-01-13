import random
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1,10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, time=current_year )


if __name__ == "__main__":
    app.run(debug=True)
