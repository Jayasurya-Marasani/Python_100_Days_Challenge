
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello World!</h1>\
            <p>This is a paragraph element....</p>\
            <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXMwc3dzdTBtaGx2MG53M2l4ZDE5YjQzcXQ4dzJwdjd0dDV2dm41OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/AbYxDs20DECQw/giphy.gif">'

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
            
    return "Bye"
@app.route("/<name>/<int:num>")
def greet(name, num):
    return f"Hello There {name} You are {num} years old"



if __name__ == "__main__":
    app.run(debug=True)

