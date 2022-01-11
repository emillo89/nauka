from flask import Flask


app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    #add few line to your code with style
    return '<h1 style="text-align: center">Hello, world!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://th.bing.com/th/id/R.77b1d50bbaf24aff4f95cd904b4e0eee?rik=KjFHBChfLdxaOw&riu=http%3a%2f%2fzoomia.pl%2ffiles%2fi%2f19%2f51%2fkoty-sprzedam-brytyjskie_big21611_19513082991331497997.jpg&ehk=n6miu7CiLV%2bc3zFDrATfEZoSS%2bukX1bEwgk5hqAjjqQ%3d&risl=&pid=ImgRaw&r=0", width=200>'


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


#Different routes using the app.route decorator
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello the {name} you are {number} years old."

#creating variable paths and converting the path to a specified data



@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye"


if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)
