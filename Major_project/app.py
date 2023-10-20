from flask import Flask, escape, request, render_template
import joblib
from sklearn.calibration import LabelEncoder
from sklearn.preprocessing import StandardScaler
import pandas as pd
model = joblib.load("model.jb")

app = Flask(__name__)
@app.route('/analysis')
def analysis():
    return render_template("stroke.html")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method =="POST":
        print(request.form)
        gender = request.form.get('gender')
        age = int(request.form['age'])
        hypertension = int(request.form['hypertension'])
        disease = int(request.form['disease'])
        married = request.form['married']
        work = request.form['work']
        residence = request.form['residence']
        glucose = (request.form['glucose'])
        bmi = (request.form['bmi'])
        smoking = request.form['smoking']
        inpdf = pd.DataFrame(
                {'gender':[gender],
                'age': [age],
                'hypertension': [hypertension],
                'heart_disease': [disease],
                'ever_married': [married],
                'work_type': [work],
                'Residence_type': [residence],
                'avg_glucose_level': [glucose],
                'bmi': [bmi],
                'smoking_status': [smoking]})
        prediction = model.predict(inpdf)[0]
        print(prediction)  
        if prediction==0:
           prediction = "NO" 
        else:
           prediction = "YES" 

        return render_template("index.html", prediction_text="Chance of Stroke Prediction is --> {}".format(prediction))   
    else:
    
        return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)




    if __name__ == "__main__":
        app.run(debug=True)