from bottle import *

# Home Page
@get('/')
def index():  
    return template('index')

# Static Routes
@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='public/js')

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='public/css')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='public/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='public/fonts')
  
# Custom Template Path and Run Server with Debug on
TEMPLATE_PATH.insert(0, "./templates/")

run(host='localhost', port='8000', debug=True, reloader=True)
