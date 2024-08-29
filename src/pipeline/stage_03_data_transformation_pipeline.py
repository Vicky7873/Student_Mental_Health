from  src.componnents.data_transformation import DataTransformation
from src.config.configuration import ConfigurationManager


class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        load_config = config.get_data_transform()
        data_transform = DataTransformation(config=load_config)
        data_transform.get_data_transform()
        data_transform.move_encoded_data()