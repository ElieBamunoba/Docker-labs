# hello world flask app
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! APP 1'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
    
#docker run -d -p 5000:5000 python-app1:latest