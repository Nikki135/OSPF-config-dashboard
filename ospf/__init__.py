from flask import Flask, render_template

def routing():
    app = Flask(__name__)
    # @app.route('/')
    # def home():
# 
        # return render_template('Lab6main.html')

    from .getconfig import getconfig
    from .ospfconfig import ospfconfig
    from .diffconfig import diffconfig
    app.register_blueprint(getconfig, url_prefix='/')
    # app.register_blueprint(getconfig)
    app.register_blueprint(ospfconfig,url_prefix='/')
    # app.register_blueprint(ospfconfig)
    # app.register_blueprint(diffconfig)
    app.register_blueprint(diffconfig,url_prefix='/')
    # app.register_blueprint(ospfconfig, url_prefix='/')
    # app.register_blueprint(diffconfig, url_prefix='/')
    return app