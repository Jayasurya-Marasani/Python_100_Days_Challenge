from flask import Flask
import random
app = Flask(__name__)
guessed_num = random.randint(0,9)

@app.route("/")
def guess_number():
    text = '<h1>Guess a number between 0 and 9</h1>\
            <img src = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt = "A Gif of Random Image">'
    return text

    
@app.route("/<int:num>")
def check_guess(num):
    if num == guessed_num:
        text = '<h1 style="color: green">You found me!</h1>\
                <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="Image for Guessing correctly">'
        return text  # Ensure this block returns the response
    elif num > guessed_num:
        text = '<h1 style="color: purple">Too high, Try Again!</h1>\
                <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="Image for High Guess">'
        return text
    else:
        text = '<h1 style="color: red">Too Low, Try Again!</h1>\
                <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="Image for Low Guess">'
        return text


if __name__ == "__main__":
    app.run(debug=True)
    