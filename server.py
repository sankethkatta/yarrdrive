#!/usr/bin/python
from bottle import *; TEMPLATE_PATH.append('templates')
from redis import StrictRedis; redis = StrictRedis(db=1)
import bottle; bottle.view = bottle.jinja2_view; bottle.template = bottle.jinja2_template
import requests

@get('/', template='index')
def index():
    return locals()

@post('/', template='upload')
def upload():
    redis.hmset(request.forms['uid'], dict(request.forms))
    return locals()


@get('/<filename:re:.+\.[a-zA-Z0-9]{2,4}>')
def serve_static(filename):
    return static_file(filename, root='./public')


@error(404)
@error(500)
def servererror(error):
    if error.exception:
        print '\033[93m', error, '\033[0m'
        return error.traceback.replace('\n', '<br>').replace(' ', '&nbsp;')
    return 'error'


port = sys.argv[1] if len(sys.argv) > 1 else 80
run(port=port, debug=True, reloader=True)
