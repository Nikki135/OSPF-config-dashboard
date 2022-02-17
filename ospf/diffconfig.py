from flask import Blueprint
from napalm import get_network_driver
# from datetime import datetime
import time
import datetime
import json
import os
# auth = Blueprint(name, import_name)
diffconfig = Blueprint('diffconfig', __name__)

@diffconfig.route('/dconfig')
def dconfig():
    # return "<p>Inside DIFF OSPF config</p>"
    # dt = datetime.datetime.now()
    # x = dt.strftime("%Y-%m-%d%H:%M:%S")
    path = "/home/netman/saveconfi/"
    devicelist = ['198.51.100.4', '198.51.101.2', '172.16.1.3', '198.51.101.4']
    # device = driver(hostname='R1_atluri',
    #     username='r1atluri',
    #     password='router1',
    #     )
    count = 0
    output1 = []
    for i in devicelist:
        count = count + 1
        print("connecting to" +str(i))
        driver = get_network_driver('ios')
        optional_args = {'secret': 'router'+str(count)}
        device = driver(i, 'r'+str(count)+'atluri', 'router'+str(count), optional_args=optional_args)
        device.open()
        
        # print("IOS OUTPU",ios_output)
        # return optional_args
        files = []
        
        print("os directory", os.listdir(path))
        for i in os.listdir(path):
            print("file",i)
        
            if 'R'+str(count)+'2022' in i:
                print("IN")
                file1 = '/home/netman/saveconfi/'+i
                ios_output = device.get_config()['running']
                device.load_merge_candidate(filename= file1)
                print("OUT")
                
                print(ios_output)
                diffs = device.compare_config()
                device.commit_config()
                print("DIFFS", diffs)
                output1.append(diffs)
                device.close()
                
    return str(output1)
                # files.append
        # with open("/home/netman/saveconfi/R"+str(count)+x, "a") as outputfile:

            # for lines in ios_output:
    # #     return lines
                # outputfile.write(lines)