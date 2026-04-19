from flask import Flask, render_template, request
from ai_model import analyze_network

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        data = request.form.get("data")
        if data:
            result = analyze_network(data)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
