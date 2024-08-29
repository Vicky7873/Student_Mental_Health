import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from src.entity import DataTransformationConfig


class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config
    
    def get_data_transform(self):
        X_train_one = self.config.X_train
        X_test_one = self.config.X_test

        X_train = pd.read_csv(X_train_one)
        X_test = pd.read_csv(X_test_one)

        le = LabelEncoder()

        for col in X_train.columns:
            if X_train[col].dtype == 'object':
                X_train[col] = le.fit_transform(X_train[col])
        
        for col in X_test.columns:
            if X_test[col].dtype == 'object':
                X_test[col] = le.fit_transform(X_test[col])

        X_train_encoded = X_train
        X_test_encoded = X_test
        print(X_train_encoded.head(2))
        return X_train_encoded, X_test_encoded
    
    def move_encoded_data(self):
        X_train_encoded,X_test_encoded = self.get_data_transform()
        if not os.path.exists(self.config.X_train_processed) and not os.path.exists(self.config.X_test_processed):
            X_train_encoded.to_csv(self.config.X_train_processed, index = False)
            X_test_encoded.to_csv(self.config.X_test_processed, index = False)
        else:
            print("Files already exists")