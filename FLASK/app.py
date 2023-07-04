from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ily")
def ily():
    return render_template("ily.html")

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0")
