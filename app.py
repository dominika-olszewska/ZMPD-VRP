import os
from urllib.request import urlopen
from flask import Flask, render_template, request
import vrp
import parseData

app = Flask(__name__)
if not os.path.isdir('./static/img'):
    os.makedirs('./static/img')


@app.route("/", methods=['GET', 'POST'])
def upload():
    dataSend = False

    if request.method == 'POST' and request.form['url'] != '':
        dataSend = True
        url = request.form['url']
        set = request.form.get('set')
        trucks = request.form['trucks']
        output = urlopen(url).read()
        file_string = (output.decode('utf-8'))
        # file_string = output.decode('ISO 8859-1')
        vehicle_distance, vehicle_load, text, filename, route_arr = vrp.cvrp(file_string, set, trucks)
        name, capacity, dimension, point_int, demand_int, trucks = parseData.parse_file(file_string, set, trucks)

        return render_template('index.html', dataSend=dataSend, file_string=text, filename=filename,
                               customers=dimension, vehicles=trucks, capacity=capacity[0], route_arr=route_arr, set=set,
                               trucks=trucks, opt_distance=sum(vehicle_distance))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
