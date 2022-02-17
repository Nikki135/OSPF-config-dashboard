from flask import Blueprint, render_template, redirect, url_for, request
from prettytable import PrettyTable
from napalm import get_network_driver
# from datetime import datetime
import time
import datetime
import json
import os
# auth = Blueprint(name, import_name)
ospfconfig = Blueprint('ospfconfig', __name__)
# data = []
@ospfconfig.route('/config', methods=['GET','POST'])
def config():
    
    
    return render_template('ospfconfig.html')
def validip(ip):
    count = len(ip.split('.'))
    d = ip.split('.')
    if count < 4 or count > 4:

        # val = False
        return False
    else:

        for i in range(count):
            if d[i] >= '0' and d[i] < '256':
                return True
                # val = True

@ospfconfig.route('/configr2', methods=['GET','POST'])
def config2():
    data1 = {
        "ipaddr": [],
        "hostname": [],
        "password":  [],
        "processid": [],
        "areaid": [],
        "net1": [],
        "net2": [],
        "loopback": []     }
    error = None
#                 print("inside validate")

                # return True
    if request.method == 'POST':
        ipadr1 = request.form['ipadr']
        data1['ipaddr'].append(request.form['ipadr'])
        data1['hostname'].append(request.form['username'])
        data1['password'].append(request.form['password'])
        data1['processid'].append(request.form['pid'])
        data1['areaid'].append(request.form['aid'])
        data1['net1'].append(request.form['net1'])
        data1['net2'].append(request.form['net2'])
        ip0 = request.form['loopback']
        val0 = validip(ip0)
        print("data1loopval", val0, ip0)
        if val0 == True:
            data1['loopback'].append(request.form['loopback'])
       
        driver = get_network_driver('ios')
        optional_args = {'secret': data1['password'][0], 'global_delaay_factor': 2}
        device = driver(data1['ipaddr'][0], data1['hostname'][0], data1['password'][0], optional_args=optional_args)
        device.open()
        x = PrettyTable()
        x.field_names = ["interface","ip"]
        b1 = validip(ipadr1)
        ips = []
        if b1 == True:
            out = json.dumps(device.get_interfaces_ip(), indent=4)
            # out1 = str(out)
            # ou1.split(f'{'ipv4': {} ')
            # out['FasEthernet0/0']
            # x.add_row()
            print("out", out)
            # print(out['ipv4'])
            # print(out1.split(','))
        # ios_output = device.get_config()['running']
        # print(ios_output)
        print("connected")
        # commands = ['router ospf 1'+data1['processid'][0], 'network '+data1['net1'][0] +' 255.255.255.0', 'network '+data1['net2'][0] +' 255.255.255.0']    
        print("inside dictionary", type(data1['processid'][0]))  
        # f = open("ospfconf.txt", "a")
        # with open("/home/netman/ospfconf.txt", "a") as outputfile:
        #     outputfile.write('router ospf'+data1['processid'][0])

            # for lines in ios_output:
        # commands = ['router ospf'+data1['processid'][0]]  
        # commands = ['router ospf 1','network 198.51.100.0 255.255.255.0' ]
        command1 = 'router ospf '+ data1['processid'][0] + '\n'+'network '+ data1['net1'][0] + ' 0.0.0.255 ' + 'area ' + data1['areaid'][0] + '\n'+'network ' + data1['net2'][0] + ' 0.0.0.255 ' + 'area ' + data1['areaid'][0] + '\n' + 'network '+ data1['loopback'][0] + ' 0.0.0.0 ' + 'area ' + data1['areaid'][0]+ '\n'+ 'exit' + '\n'
        print("command", command1)
        res = device.load_merge_candidate(config= command1)
        print("result",res)
        diffs = device.compare_config()
        if len(diffs) > 0:
            print("Output", diffs)
            device.commit_config()
            time.sleep(5)
        else:
            device.discard_config()
        # device.commit_config()
        # if len()
        print("output", device.compare_config())
        print(data1)
        return render_template('ospfr2.html')
        # device.close()
        # res = device.load_merge_candidate(filename= '/home/netman/ospfconf.txt')
        # ios_output = device.get_config()['running']

        # res = device.cli(commands)
        # prettytables(data1)
        # print("output",res)
      
        # console.log()
        # config3(data)

@ospfconfig.route('/configr3', methods=['GET','POST'])
def config3():
    # data2 = []
    data2 = {
        "ipaddr": [],
        "hostname": [],
        "password":  [],
        "processid": [],
        "areaid1": [],
        "areaid2": [],
        "net1": [],
        "net2": [],
        "loopback": []     }
    error = None
    if request.method == 'POST':
        data2['ipaddr'].append(request.form['ipadr2'])
        data2['hostname'].append(request.form['username2'])
        data2['password'].append(request.form['password2'])
        data2['processid'].append(request.form['pid2'])
        data2['areaid1'].append(request.form['aid1'])
        data2['areaid2'].append(request.form['aid2'])
        data2['net1'].append(request.form['net1'])
        data2['net2'].append(request.form['net2'])
        ip2 = request.form['loopback2']
        val2 = validip(ip2)
        print("data2val", val2, ip2)
        if val2 == True:
            data2['loopback'].append(request.form['loopback2'])
        # data2.append(request.form['loopback2'])
        driver = get_network_driver('ios')
        optional_args = {'secret': data2['password'][0]}
        device = driver(data2['ipaddr'][0], data2['hostname'][0], data2['password'][0], optional_args=optional_args)
        device.open()
        # ios_output = device.get_config()['running']
        # print(ios_output)
        print("connected")
        command1 = 'router ospf '+ data2['processid'][0] + '\n'+'network '+ data2['net1'][0] + ' 0.0.0.255 ' + 'area ' + data2['areaid1'][0] + '\n'+'network ' + data2['net2'][0] + ' 0.0.0.255 ' + 'area ' + data2['areaid2'][0] + '\n' + 'network '+ data2['loopback'][0] + ' 0.0.0.0 ' + 'area ' + data2['areaid1'][0]+'\n' + 'end'
        print("command", command1)
        device.load_merge_candidate(config= command1)
        print("output", device.compare_config())
        device.commit_config()
        device.close()
        # res = device.load_merge_candidate(filename= '/home/netman/ospfconf.txt')
        # ios_output = device.get_config()['running']

        # res = device.cli(commands)
        # prettytables(data2)
        # print("output",res)
        
        # prettytables(data2)
        print(data2)
        return render_template('ospfr3.html')
        # config4(data)

@ospfconfig.route('/configr4', methods=['GET','POST'])
def config4():
    data3 = {
        "ipaddr": [],
        "hostname": [],
        "password":  [],
        "processid": [],
        "areaid": [],
        "net1": [],
        "loopback": []     }
    error = None
    if request.method == 'POST':
        data3['ipaddr'].append(request.form['ipadr3'])
        data3['hostname'].append(request.form['username3'])
        data3['password'].append(request.form['password3'])
        data3['processid'].append(request.form['pid3'])
        data3['areaid'].append(request.form['aid3'])
        data3['net1'].append(request.form['net3'])
        ip3 = request.form['loopback3']
        val3 = validip(ip3)
        print("data3val", val3, ip3)
        if val3 == True:
            data3['loopback'].append(request.form['loopback3'])
        # data3.append(request.form['loopback3'])
        driver = get_network_driver('ios')
        optional_args = {'secret': data3['password'][0]}
        device = driver(data3['ipaddr'][0], data3['hostname'][0], data3['password'][0], optional_args=optional_args)
        # command1 = 'router ospf '+ data3['processid'][0] + '\n'+'network '+ data3['net1'][0] + ' 0.0.0.255 ' + 'area ' + data3['areaid'][0] + '\n'
        device.open()
        # ios_output = device.get_config()['running']
        # print(ios_output)
        print("connected")

        # commands = ['router ospf 1'+data3['processid'][0], 'network '+data3['net1'][0] +' 255.255.255.0', 'network '+data3['net2'][0] +' 255.255.255.0']    

        # print("inside dictionary", type(data1['processid'][0]))  
        # f = open("ospfconf.txt", "a")
        # with open("/home/netman/ospfconf.txt", "a") as outputfile:
        #     outputfile.write('router ospf'+data1['processid'][0])

            # for lines in ios_output:
        # commands = ['router ospf'+data1['processid'][0]]  
        # commands = ['router ospf 1','network 198.51.100.0 255.255.255.0' ]
        print("data3", data3)
        command1 = 'router ospf '+ data3['processid'][0] + '\n'+'network '+ data3['net1'][0] + ' 0.0.0.255 ' + 'area ' + data3['areaid'][0] + '\n' + 'network '+ data3['loopback'][0] + ' 0.0.0.0 ' + 'area ' + data3['areaid'][0]
        print("command", command1)
        device.load_merge_candidate(config= command1)
        print("output", device.compare_config())
        device.commit_config()
        device.close()
       
        # prettytables(data3)
        print(data3)
        return render_template('ospfr4.html')
        # configured(data)
        # console.log(data3)

@ospfconfig.route('/configured', methods=['GET','POST'])
def configured():
   
    data4 = {
        "ipaddr": [],
        "hostname": [],
        "password":  [],
        "processid": [],
        "areaid1": [],
        "areaid2": [],
        "net1": [],
        "net2": [],
        "loopback": []  
        }
    error = None
    if request.method == 'POST':
        data4['ipaddr'].append(request.form['ipadr4'])
        data4['hostname'].append(request.form['username4'])
        data4['password'].append(request.form['password4'])
        data4['processid'].append(request.form['pid4'])
        data4['areaid1'].append(request.form['aid41'])
        data4['areaid2'].append(request.form['aid42'])
        data4['net1'].append(request.form['net41'])
        data4['net2'].append(request.form['net42'])
        ip4 = request.form['loopback4']
        val4 = validip(ip4)
        if val4 == True:
            data4['loopback'].append(request.form['loopback4'])
        driver = get_network_driver('ios')
        optional_args = {'secret': data4['password'][0]}
        device = driver(data4['ipaddr'][0], data4['hostname'][0], data4['password'][0], optional_args=optional_args)
        device.open()
        # ios_output = device.get_config()['running']
        # print(ios_output)
        print("connected" , data4)
        command1 = 'router ospf '+ data4['processid'][0] + '\n'+'network '+ data4['net1'][0] + ' 0.0.0.255 ' + 'area ' + data4['areaid1'][0] + '\n'+'network ' + data4['net2'][0] + ' 0.0.0.255 ' + 'area ' + data4['areaid2'][0] + '\n' 'network '+ data4['loopback'][0] + ' 0.0.0.0 ' + 'area ' + data4['areaid1'][0] + '\n' +'end'
        print("command", command1)
        device.load_merge_candidate(config= command1)
        print("output", device.compare_config())
        device.commit_config()
        time.sleep(5)
        device.close()
        print(data4)
        ret = "OSPF Successfully configured"
        return ret
     
def prettytables(data):

    x = PrettyTable()
    x.field_names = ["username","password", "processid", "AreaId","Loopback"]
    host = data['hostname']
    passw = data['password']
    prid = data['processid']
    arid = data['areaid']
    loop = data['loopback']
    x.add_row([host, passw, prid, arid, loop])
    print(x)
    return x


# @ospfconfig.route('/configfinal')
# def config():
#     return render_template('ospfconfig.html')
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect(url_for('home'))
#     return render_template('login.html', error=error)