from flask import Flask
# from  markupsafe import escape

app = Flask(__name__)
print(__name__)
@app.route('/')
def hello_world():
    return "Hello, world!"

@app.route("/bye")
def bye():
    return "Bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello the {name} you are {number} years old."

if __name__ == "__main__":
    app.run(debug=True)
