# init Flask object start up webservice
from appconfig import app

if __name__ == '__main__':
    app.run(host='localhost', port=1234, debug=True)