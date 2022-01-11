from flask import Flask
# from  markupsafe import escape

app = Flask(__name__)
print(__name__)
@app.route('/')
def hello_world():
    return "Hello, world!"

#Different routes using the app.route decorator
@app.route("/bye")
def bye():
    return "Bye"

#creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello the {name} you are {number} years old."

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)
