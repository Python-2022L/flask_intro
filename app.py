from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    html = """
    <form action="http://127.0.0.1:8080/api/get-sum">
    <label>a:</label><br>
    <input type="text"  name="a" value="0"><br>
    <label>b:</label><br>
    <input type="text" name="b" value="0"><br><br>
    <input type="submit" value="Submit">
    </form>
    """
    return html

@app.route("/api/get-sum")
def sum():
    print(request.form)
    args = request.args
    a = args.get('a', 0)
    b = args.get('b', 0)
    
    return {"sum": int(a) + int(b)}

if __name__ == '__main__':
    app.run(debug=True, port='8080')