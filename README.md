# Student_Mental_Health

### scenarios:
<!-- 
Predicting Mental Health Outcomes:

Target Variable: depression, anxiety, or isolation
Use Case: You might want to predict whether a student is likely to experience depression, anxiety, or isolation based on their academic and social factors.
Predicting Academic Performance:

Target Variable: cgpa
Use Case: You might want to predict a student's CGPA based on their background, academic workload, and other factors.
Predicting Study Satisfaction:

Target Variable: study_satisfaction
Use Case: You might want to predict how satisfied a student is with their studies based on various factors such as academic pressure, financial concerns, and social relationships.
Predicting Future Insecurity:

Target Variable: future_insecurity
Use Case: You might want to predict how insecure a student feels about their future based on their academic and social experiences. -->

### For me we will treated depression as tagret variable

Value 1: Represents the lowest depression (no depression).
Value 5: Represents a major depression as per Google.




1. conda create -n studentMH python=3.12 -y
2. Install the requirements for EDA
pip install -r requirement.txt
3. EDA Starts
4. Feature Engennering

Label Encoding: university, degree_major, residential_status,campus_discrimination
Ordinal Encoding: degree_level, academic_year, cgpa, average_sleep, sports_engagement

for gender i have assign the unique values manually

#### 5. Feature selection
Using scikit-learn for Feature Selection
Feature selection techniques can help address multicollinearity indirectly by selecting relevant features.

from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(x)
# Apply feature selection
selector = SelectKBest(score_func=f_classif, k='all')
selector.fit(X_scaled, y)
scores = selector.scores_

# Create a DataFrame with feature scores
feature_scores = pd.DataFrame({'Feature': x.columns, 'Score': scores})
print(feature_scores)


6. Model BUilding
Logistic regression
random forest
XGboost

Randomforest we will chose based on our score

 # Create the project structure
 1. Temp.py
 few cmds for vscode terminal execution
 mkdir insights -> create folder using vs code terminal
 touch main.py  -> create files using vs code terminal
 mv insights.txt insights/ -> move files from one folder to another folder

 # Workflows
 1. Update config.yaml
here we will store the config things example data set path to get the data/store the data etc
2. Update params.yaml
3. Update entity
entity is nothing but the return type of a function
entity where we just store the data paths only, once configuration manager will execute then it will return the and store the data as per the entity data storage path
4. Update the configuration manager in src config
configuration manager where we will read the config/params yaml and and return the data to the entity folder, this will used in pipeline 
5. update the components
this .py file will zip unzip the data and store the data into the respective folder, once the configuration manager will execute then it will return the and store the data as per the entity data storage path
6. update the pipeline

7. update the main.py
to run the pipe line we need write the pieace of code
8. update the app.py

# Docker 
1. run the application on local docker
docker build -t smh .
smh is my image name
#### it will create an local image
2. docker run -p 5000:5000 your-image-name
#### run the docker file

# 1. Login to AWS console.
# 2. Create IAM user for deployment

#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

# Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
3. Create ECR repo to store/save docker image
- Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/text-s
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
# 6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one
# 7. Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app

