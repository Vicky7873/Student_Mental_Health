from src.config.configuration import ConfigurationManager
from src.componnents.data_loading import DataLoading 

class DataLoadingPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        data_loading_config = config_manager.get_data_loading_config()
        data_loader = DataLoading(config=data_loading_config)
        df = data_loader.get_data_loading()
        data_loader.save_data()