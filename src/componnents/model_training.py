from sklearn.ensemble import RandomForestClassifier
import pickle
import pandas as pd
from src.entity import ModelTrainingConfig


class ModelTrainer:
    def __init__(self,config:ModelTrainingConfig):
        self.config = config

    def model_building(self):
        rfc = RandomForestClassifier(n_estimators=self.config.n_estimators,criterion=self.config.criterion)
        return rfc

    def model_training(self):
        rfc =self.model_building()
        X_train = pd.read_csv(self.config.X_train_processed)
        y_train = pd.read_csv(self.config.y_train_processed)
        model = rfc.fit(X_train, y_train)
        pickle.dump(model, open(self.config.model_path, 'wb'))
        model.score(X_train, y_train)
        return model