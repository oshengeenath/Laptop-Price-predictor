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

        feature_list = []
        feature_list.append(int('Ram'))
        feature_list.append(float('Weight'))
        feature_list.append(len('Touchscreen'))
        feature_list.append(len('IPS'))

        company_list = ['Company_Acer', 'Company_Apple','Company_Asus', 'Company_Dell', 'Company_HP', 'Company_Lenovo','Company_MSI', 'Company_Other', 'Company_Toshiba']
        typename_list = ['TypeName_2 in 1 Convertible', 'TypeName_Gaming', 'TypeName_Netbook','TypeName_Notebook', 'TypeName_Ultrabook', 'TypeName_Workstation']
        opsys_list = ['OpSys_Linux', 'OpSys_Mac', 'OpSys_Others', 'OpSys_Windows']
        cpu_list = ['CPU_name_AMD', 'CPU_name_Intel Core i3', 'CPU_name_Intel Core i5','CPU_name_Intel Core i7', 'CPU_name_Others']
        gpu_list = ['GPU_name_AMD','GPU_name_Intel', 'GPU_name_Nvidia']



    return render_template('index.HTML')

if __name__ == '__main__':
    app.run(debug=True)
