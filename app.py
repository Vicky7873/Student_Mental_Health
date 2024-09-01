import os
from flask import Flask, render_template, request
from sklearn.preprocessing import LabelEncoder
import pandas as pd 
import pickle


app = Flask(__name__, template_folder='templates')
model = pickle.load(open('/Users/bhikipallai/Desktop/Projects/Student_Mental_Health/Student_Mental_Health/data/model_training/rfc.pkl',"rb"))

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        gender = request.form.get('gender')
        age = int(request.form.get('age'))
        university = request.form.get('university')
        degree_level = request.form.get('degree_level')
        degree_major = request.form.get('degree_major')
        academic_year = request.form.get('academic_year')
        cgpa = request.form.get('cgpa')
        residential_status = request.form.get('residential_status')
        campus_discrimination = request.form.get('campus_discrimination')
        sports_engagement = request.form.get('sports_engagement')
        average_sleep = int(request.form.get('average_sleep'))
        study_satisfaction = int(request.form.get('study_satisfaction'))
        academic_workload = int(request.form.get('academic_workload'))
        academic_pressure = int(request.form.get('academic_pressure'))
        financial_concerns = int(request.form.get('financial_concerns'))
        social_relationships = int(request.form.get('social_relationships'))
        anxiety = int(request.form.get('anxiety'))
        isolation = int(request.form.get('isolation'))
        future_insecurity = int(request.form.get('future_insecurity'))

        # Make DataFrame from the form data
        Data = pd.DataFrame({
            'gender': [gender],
            'age': [age],
            'university': [university],
            'degree_level': [degree_level],
            'degree_major': [degree_major],
            'academic_year': [academic_year],
            'cgpa': [cgpa],
            'residential_status': [residential_status],
            'campus_discrimination': [campus_discrimination],
            'sports_engagement': [sports_engagement],
            'average_sleep':[average_sleep],
            'study_satisfaction': [study_satisfaction],
            'academic_workload': [academic_workload ],
            'academic_pressure': [academic_pressure],
            'financial_concerns': [financial_concerns],
            'social_relationships': [social_relationships],
            'anxiety':[anxiety],
            'isolation':[isolation],
            'future_insecurity':[future_insecurity]
        })


        # Preprocess the data
        label_encoder = LabelEncoder()
        cat_cols = ['gender','university','degree_level', 'degree_major', 'academic_year', 'cgpa', 'residential_status', 'campus_discrimination', 'sports_engagement', 'average_sleep']
        Data[cat_cols] = Data[cat_cols].apply(label_encoder.fit_transform)

        Data = Data.fillna(0)

        my_pred = model.predict(Data)

        if my_pred == 1:
            prediction = 'You are healthy'
        elif my_pred == 2:
            prediction = 'You are healthy'
        elif my_pred == 3:
            prediction = 'Please take care of your health and contact to your Doctor if required '
        elif my_pred == 4:
            prediction = 'Sorry! Please contact to your Doctor'
        elif my_pred == 5:
            prediction = 'Sorry! Please contact to your Doctor'
        

        # Render the result
        return render_template('result1.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True,port = 8080,host = '0.0.0.0')