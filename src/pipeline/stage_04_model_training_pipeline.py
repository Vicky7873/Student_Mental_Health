from src.config.configuration import ConfigurationManager
from src.componnents.model_training import ModelTrainer


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer = config.get_model_training_config()
        model = ModelTrainer(config=model_trainer)
        model.model_building()
        model.model_training()