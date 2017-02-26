import pyttsx
import base64
import os
from flask import Flask ,request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.form['imgBase64']
        f1 = f.split(',')[1]
        f2 = base64.decodestring(f1)
        fi = open('/home/rj/Downloads/openface-master/img.png', 'w')
        fi.write(f2)
        fi.close()
        os.system('python /home/rj/Downloads/openface-master/try.py infer')
        f3 = open('/home/rj/Downloads/openface-master/myfile', 'r')
        va=f3.read();
        detec=va.split(' ')[0]

        engine = pyttsx.init()
        engine.say(str(detec) + 'is on the door')
        engine.runAndWait()
        if(float(va.split(' ')[1])<0.6):
            return "naam pucho"
        return 'hello ' +str(detec)
        #f.save('/home/rj/Downloads/openface-master/img.png')


@app.route('/setname', methods=['GET', 'POST'])
def setname():
    if request.method == 'POST':
        f1 = request.form['name']
        print "yaha pahu"
        os.system('python /home/rj/Downloads/openface-master/try.py savit '+str(f1))
        return 'hello ' +str(f1)
    return 'sesf'
