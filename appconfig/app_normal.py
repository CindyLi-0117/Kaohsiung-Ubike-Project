# all flask web is in this module
from appconfig import app

@app.route('/')
@app.route('/home')
def home():
    return '<h3>Home Page</h3>'