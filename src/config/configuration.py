# for configmanger
from src.constants import *
from src.utils.common import read_yaml, create_directories
from src.entity import DataIngestionConfig, DataloadingConfig



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
