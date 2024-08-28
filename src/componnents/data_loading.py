import os
import zipfile
import urllib.request as request
import pandas as pd
from src.logging import logger
from src.componnents.data_ingestion import DataIngestion
from src.entity import DataIngestionConfig
from sklearn.model_selection import train_test_split
from src.entity import DataloadingConfig
import os
class DataLoading:
    def __init__(self, config: DataloadingConfig):
        self.config = config

    def get_data_loading(self):
        config2 = DataIngestionConfig(root_dir=self.config.root_dir, data_path=self.config.data_path)
        data_ingestion = DataIngestion(config2)
        df = data_ingestion.get_data()
        return df
    
    def split_data(self):
        df = self.get_data_loading()
        X = df.drop('depression',axis=1)
        y = df['depression']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.config.test_size, random_state=42)
        return X_train, X_test, y_train, y_test

    def save_data(self):
        X_train, X_test, y_train, y_test = self.split_data()
        # if file exists skip else create it
        if not os.path.exists(self.config.X_train) and not os.path.exists(self.config.y_train) and not os.path.exists(self.config.X_test) and not os.path.exists(self.config.y_test):
            X_train.to_csv(self.config.X_train, index = False)
            X_test.to_csv(self.config.X_test, index = False)
            y_train.to_csv(self.config.y_train, index = False)
            y_test.to_csv(self.config.y_test, index = False)
        else:
            print("Files already exist")
