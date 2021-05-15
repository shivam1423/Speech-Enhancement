from flask import Flask
app = Flask(__name__)
import os
from flask import jsonify
from flask import render_template,request
#from VQA import predict
from main import prediction_mode
import sys
import random
import string
import io
UPLOAD_FOLDER = 'upload_audios/input/'
OUTPUT_FOLDER = 'static/'
@app.route("/", methods = ['GET', 'POST'])
def home():
    print ("Hello")
    print (request.args,request.form)
    if request.method == 'POST':
        if request.files['file'].filename == '':
            print ("NO Files Uploaded")
            return "oops"
        else:
            file1 = request.files['file']
            print ("POST FORM")         
            temp = os.path.join(UPLOAD_FOLDER, ''.join(request.files['file'].filename))
            print(temp)
            file1.save(temp)
            #result = predict(temp,ques)
            prediction_mode(UPLOAD_FOLDER,request.files['file'].filename,OUTPUT_FOLDER)
            os.remove(temp)
            #return jsonify(result=result,success=True)
            print(os.path.join(OUTPUT_FOLDER, ''.join(request.files['file'].filename)))
            return jsonify(result=os.path.join(OUTPUT_FOLDER, ''.join(request.files['file'].filename)),success=True)
        
            
    else:
        return render_template('index.html')
sys.stdout.flush()
