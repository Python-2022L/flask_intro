from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return "HOME"

@app.route("/api/get-sum")
def sum():
    args = request.args
    a = args.get('a', 0)
    b = args.get('b', 0)
    
    return {"sum": int(a) + int(b)}

if __name__ == '__main__':
    app.run(debug=True, port='8080')