import pickle
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from src.entity import ModelEvaluatioConfig

class ModelEvaluate:
    def __init__(self,config:ModelEvaluatioConfig):
        self.config = config

    
    def metrics(self,actual,prediction):
        acc_score = accuracy_score(actual, prediction)
        conf_matrix = confusion_matrix(actual, prediction)
        class_report = classification_report(actual, prediction)
        return acc_score, conf_matrix, class_report
    
    def model_score(self):
        model = pickle.load(open(self.config.model_path, 'rb'))
        X_test = pd.read_csv(self.config.X_test_processed)
        self.y_test = pd.read_csv(self.config.y_test_processed)

        self.y_pred = model.predict(X_test)
        print(f"Model Accuracy Score: {accuracy_score(self.y_test, self.y_pred)}")
        print(f"Model Confusion Matrix: {confusion_matrix(self.y_test, self.y_pred)}")
        print(f"Model Classification Report: {classification_report(self.y_test, self.y_pred)}")

    
    def save_metrics(self):
        (acc_score, conf_matrix, class_report) = self.metrics(self.y_test, self.y_pred)
        with open(self.config.save_param, 'w') as f:
            f.write(f"acc Score: {acc_score}\n")
            f.write(f"Confusion Matrix: {conf_matrix}\n")
            f.write(f"Classification Report: {class_report}\n")