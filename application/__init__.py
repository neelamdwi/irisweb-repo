from flask import Flask, render_template, request, json
import requests

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/irisclassify", methods=['GET', 'POST'])
def irisclassify():
   
    # extract form inputs 
    sepallength = request.form.get("sepallength")
    sepalwidth = request.form.get("sepalwidth")
    petallength = request.form.get("petallength")
    petalwidth = request.form.get("petalwidth")
    
    #url for irisservice
    #url = "http://localhost:5000/api"
    url = "https://irismodel-app.herokuapp.com/api"

    #create json from form inputs
    data = json.dumps({"sepallength": sepallength, "sepalwidth": sepalwidth, "petallength": petallength, "petalwidth": petalwidth})

    #post json to url
    results =  requests.post(url,data)
    
    #send features and prediction result to index.html for display
    return render_template("index.html", sepallength = sepallength, sepalwidth = sepalwidth, petallength = petallength, petalwidth = petalwidth, results=results.content.decode('UTF-8'))
  