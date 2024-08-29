from src.logging import logger
from src.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline
from src.pipeline.stage_02_data_loading_pipeline import DataLoadingPipeline
from src.pipeline.stage_03_data_transformation_pipeline import DataTransformationPipeline
from src.pipeline.stage_04_model_training_pipeline import ModelTrainingPipeline
from src.pipeline.stage_05_model_evalution_pipeline import Model_Evaluation_Pipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Loading Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataLoadingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj =Model_Evaluation_Pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e