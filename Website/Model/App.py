import requests
from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        ram = request.form["ram"]
        weight = request.form["weight"]
        company = request.form["company"]
        typename = request.form["typename"]
        opsys = request.form["opsys"]
        cpu = request.form["cpuname"]
        gpu = request.form["gpuname"]
        touchscreen = request.form.getlist("touchscreen")
        ips = request.form.getlist("ips")

    return render_template('index.HTML')

if __name__ == '__main__':
    app.run(debug=True)
