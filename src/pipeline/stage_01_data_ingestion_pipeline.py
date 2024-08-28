from src.config.configuration import ConfigurationManager
from src.componnents.data_ingestion import DataIngestion



class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager().get_data_ingestion_config()
        data_ingestion = DataIngestion(config)
        data_ingestion.move_file_to_data_ingestion()
        data_ingestion.get_data()
