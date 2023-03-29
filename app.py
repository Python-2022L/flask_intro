from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return """
    /home
    /about
    """

@app.route("/product")
def home():
    return {
        "name":"Samsung",
        "color":"blue",
        "ram":64
    }

@app.route('/about')
def about():
    return "About Page"

app.run(debug=True, port='4180')