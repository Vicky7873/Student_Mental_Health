# for configmanger
from src.constants import *
from src.utils.common import read_yaml, create_directories
from src.entity import DataIngestionConfig, DataloadingConfig, DataTransformationConfig, ModelTrainingConfig



class ConfigurationManager:
    def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.data_root])
    
    def get_data_ingestion_config(self):
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )
    
        return data_ingestion_config
    

    def get_data_loading_config(self) -> DataloadingConfig:
        config = self.config.data_loading
        params = self.params.test_size_args
        create_directories([config.root_dir])
        data_loading_config = DataloadingConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            X_train = config.X_train,
            y_train = config.y_train,
            X_test = config.X_test,
            y_test = config.y_test,
            test_size = params.test_size,
        )
        return data_loading_config
    

    def get_data_transform(self)->DataTransformationConfig:
        config = self.config.data_preprocessing

        create_directories([config.root_dir])
        data_transform_config = DataTransformationConfig(
            root_dir = config.root_dir,
            X_train = config.X_train,
            X_test = config.X_test,
            y_train = config.y_train,
            y_test = config.y_test,
            X_train_processed = config.X_train_processed,
            X_test_processed = config.X_test_processed,
            y_train_processed = config.y_train_processed,
            y_test_processed = config.y_test_processed
        )
        return data_transform_config


    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config.model_training
        params = self.params.model_args
        create_directories([config.root_dir])
        model_training_config = ModelTrainingConfig(
            root_dir = config.root_dir,
            model_path = config.model_path,
            criterion = params.criterion,
            n_estimators = params.n_estimators,
            X_train_processed= config.X_train_processed,
            y_train_processed = config.y_train_processed
        )
        return model_training_config
