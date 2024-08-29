from src.componnents.model_evaluation import ModelEvaluate
from src.config.configuration import ConfigurationManager


class Model_Evaluation_Pipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluate(config = model_evaluation_config)
        model_evaluation.model_score()
        model_evaluation.save_metrics()