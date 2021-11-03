from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def bugReport():
    return render_template("bugReport.html")

if __name__ == "__main__":
    app.run(debug=True)