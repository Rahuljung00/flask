from flask import Flask, render_template, request , redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/away", methods=["GET", "POST"])
def home():
    name = ""
    if request.method == "POST":
        name = request.form.get("name")
    return redirect(url_for("display",name = name))

@app.route("/display<name>")
def display(name):
    return f" hey whats up {name}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)

