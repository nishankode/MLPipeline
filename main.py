# Training pipeline entry point
from src.datascienceproject import logger

from src.datascienceproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascienceproject.pipeline.data_validation_pipeline import DataValidationPipeline
from src.datascienceproject.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.datascienceproject.pipeline.model_training_pipeline import ModelTrainingPipeline


if __name__ == "__main__":

    # Running Data Ingestion Training pipeline
    try:
        STAGE_NAME = 'Data Ingestion Stage'
        logger.info(f">>>>>> Stage Started : {STAGE_NAME} <<<<<<")
        data_injestion_train_obj = DataIngestionTrainingPipeline()
        data_injestion_train_obj.initiate_data_ingestion()
        logger.info(f">>>>>> Stage Completed : {STAGE_NAME} <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

    # Running Data Validation Pipeline
    try:
        STAGE_NAME = 'Data Validation Stage'
        logger.info(f">>>>>> Stage Started : {STAGE_NAME} <<<<<<")
        data_validation_pipeline_obj = DataValidationPipeline()
        data_validation_pipeline_obj.initiate_data_validation()
        logger.info(f">>>>>> Stage Completed : {STAGE_NAME} <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

    # Running Data Transformation Pipeline
    try:
        STAGE_NAME = 'Data Transformation Stage'
        logger.info(f">>>>>> Stage Started : {STAGE_NAME} <<<<<<")
        data_transformation_pipeline_object = DataTransformationPipeline()
        data_transformation_pipeline_object.initiate_data_transformaiton()
        logger.info(f">>>>>> Stage Completed : {STAGE_NAME} <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    
    # Running Model Training pipeline
    try:
        STAGE_NAME = 'Model Training Stage'
        logger.info(f">>>>>> Stage Started : {STAGE_NAME} <<<<<<")
        model_training_pipeline_object = ModelTrainingPipeline()
        model_training_pipeline_object.initiate_model_training()
        logger.info(f">>>>>> Stage Completed : {STAGE_NAME} <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e