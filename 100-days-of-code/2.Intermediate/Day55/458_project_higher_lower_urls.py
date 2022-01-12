from flask import Flask
import random

app = Flask(__name__)

number = random.randint(0, 9)
print(number)


@app.route("/")
def home():
    return "<h1> Guess a number between 0 and 9 </h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > number:
        return "<h1 style='color: purple'>Too high! </h1>" \
               "<img src='https://giphy.com/gifs/animation-walt-disney-mickey-mouse-l2JhL0Gpfbvs4Y07K'>"
    elif guess < number:
        return "<h1 style='color: red'>Too low! </h1>" \
               "<img src='https://giphy.com/gifs/lips-LlpTxmiJngXpS'>"
    else:
        return "<h1 style='color: red'>You find me! </h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)

print("hahha")