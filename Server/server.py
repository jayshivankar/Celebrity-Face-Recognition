from flask import Flask,request,jsonify
import utils
app = Flask(__name__)

@app.route('/classify image',methods = ['GET','POST'])
def classify_image():
    image_data = request.form['image_data']

    response =  jsonify(utils.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__=="__main__":
    app.run(port=5000)