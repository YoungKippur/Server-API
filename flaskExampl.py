from flask import Flask
from flask import request
import datetime
  
app = Flask(__name__)

@app.route('/')
def hello_world():
    print(request.__dict__['method'])
    print(request.__dict__['path'])
    print(datetime.datetime.now())
    return 'Hello World'
  
if __name__ == '__main__':
    app.run()