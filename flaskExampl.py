from flask import Flask, request, jsonify
import datetime
import serial
  
app = Flask(__name__)

PORT = input("Ingrese el puerto serie: ")
serialEsp = serial.Serial(PORT, 115200)

@app.route('/')
def hello_world():
    # print(request.__dict__['method'])
    # print(request.__dict__['path'])
    # print(datetime.datetime.now())
    return 'The Server Is Online (●*◡*●) Y.K'
    sendSerial = (request.__dict__['method'] + "," + request.__dict__['path'] + "," + str(datetime.datetime.now()))
    serialEsp.write(sendSerial.encode('ascii'))
  
@app.route('/api')
def apiExample():
    return jsonify({"message" : "API is working!!", "time" : str(datetime.datetime.now())})
    # serialEsp.write(sendSerial.encode('ascii'))
  
if __name__ == '__main__':
    app.run()
