from flask import Flask

app = Flask(__name__)

TEXTS = {
    "home" : "welcome home",
    "back" : "welcome back",
}

@app.get('/welcome')
def say_welcome():
    """ Return simple "welcome" greeting. """
    html = "<html><body><h1>welcome</h1></body></html>"
    return html


@app.get('/welcome/<greet>')
def say_welcome_text(greet):
    """ Return simple "welcome home" greeting. """
    greeting = TEXTS.get(greet)
    # greeting = TEXTS[greet]
    return f"<html><body><h1>{greeting}</h1></body></html>"
