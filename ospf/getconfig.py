from flask import Flask, render_template, Blueprint
from napalm import get_network_driver
# from datetime import datetime
import datetime
import json
import os
# from templates import Lab6main
# app = Flask(__name__)


# @app.route('/getconfig')
# def getconfig():
#     print("inin")
    
#     return render_template('getconfig.html')

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Blueprint
# auth = Blueprint(name, import_name)
getconfig = Blueprint('getconfig', __name__)
@getconfig.route('/')
def home():
    return render_template("index.html")
    # return "<h1>TEST</h1>"

@getconfig.route('/gconfig')
def gconfig():
    dt = datetime.datetime.now()
    x = dt.strftime("%Y-%m-%d%H:%M:%S")
    path = "/home/netman/saveconfi"
    devicelist = ['198.51.100.4', '198.51.101.2', '172.16.1.3', '198.51.101.4']
    # device = driver(hostname='R1_atluri',
    #     username='r1atluri',
    #     password='router1',
    #     )
    count = 0
    for i in devicelist:
        count = count + 1
        print("connecting to" +str(i))
        driver = get_network_driver('ios')
        optional_args = {'secret': 'router'+str(count)}
        device = driver(i, 'r'+str(count)+'atluri', 'router'+str(count), optional_args=optional_args)
        device.open()
        ios_output = device.get_config()['running']
        # return optional_args
        with open("/home/netman/saveconfi/R"+str(count)+x+'.txt', "a") as outputfile:

            for lines in ios_output:
    # #     return lines
                outputfile.write(lines)
    
    # devicelist =
    # device = driver('198.51.100.4', 'r1atluri', 'router1',optional_args=optional_args)
    # print("opening")
    # device.open()
    # ios_output = device.get_config()['running']
    # res = type(ios_output)
    # with open("/home/netman/saveconfi/ospf1.txt","a") as outputfile:
        
    dir_list = os.listdir(path)

    return str(dir_list)
    # obj = json.loads(str(ios_output))
    # return json.dumps(obj, indent=4)
    # return str(dir_list)
    # return ios_output
    # y=device.cli(['show run'])
    # data = []
    # data.append(y.split('/n'))
    # return data