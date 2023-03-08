from flask import Flask
app = Flask(__name__)



@app.get('/<operation>'):
    def calculator (<operation>):
    """Returns calculation for operation variable"""

    html = <html><body><h1></h1></body></html>


