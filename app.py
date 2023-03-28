from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return {"ok":True}

app.run(debug=True, port='4180')