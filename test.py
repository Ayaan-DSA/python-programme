from flask import Flask

app = Flask(__name__)

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"The sum of {a} and {b} is {a + b}"
@app.route('/hello/<name>')
def greet(name) :
    return f"Hello World {name}"
@app.route('/product/<int:c>/<int:d>')
def product(c,d):

    return f"The product of {c} and {d} is {c*d}"
@app.route('/handle_url_params')
def handle_params():
    return str(request.args)
if __name__ == "__main__":
    app.run(debug=True)
