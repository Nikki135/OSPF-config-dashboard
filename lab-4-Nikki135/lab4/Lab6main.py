from flask import Flask, render_template
# from getconfig import getconfig
from ospf import routing
# from OSP
app = routing()


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000, debug=True)