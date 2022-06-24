from flask import Flask, request, jsonify
import datetime
  
app = Flask(__name__)

@app.route('/')
def hello_world():
    # print(request.__dict__['method'])
    # print(request.__dict__['path'])
    # print(datetime.datetime.now())
    return 'The Server Is Online (●*◡*●) Y.K'
  
@app.route('/api')
def apiExample():
    return jsonify({"message" : "API is working!!", "time" : str(datetime.datetime.now())})

if __name__ == '__main__':
    app.run()