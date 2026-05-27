# Training pipeline entry point
from src.datascienceproject import logger

from prefect import task, flow

from src.datascienceproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascienceproject.pipeline.data_validation_pipeline import DataValidationPipeline
from src.datascienceproject.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.datascienceproject.pipeline.model_training_pipeline import ModelTrainingPipeline
from src.datascienceproject.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


# Running Data Ingestion Training Pipeline
@task(name='Data Ingestion', retries=2, retry_delay_seconds=10)
def data_ingestion():
    STAGE_NAME = 'Data Ingestion Stage'
    logger.info(f">>>>>> Stage Started : {STAGE_NAME} <<<<<<")
    data_injestion_train_obj = DataIngestionTrainingPipeline()
    data_injestion_train_obj.initiate_data_ingestion()
    logger.info(f">>>>>> Stage Completed : {STAGE_NAME} <<<<<<")


# Running Data Validation Pipeline
@task(name='Data Validation')
def data_validation():
    STAGE_NAME = 'Data Validation Stage'
    logger.info(f">>>>>> Stage Started : {STAGE_NAME} <<<<<<")
    data_validation_pipeline_obj = DataValidationPipeline()
    data_validation_pipeline_obj.initiate_data_validation()
    logger.info(f">>>>>> Stage Completed : {STAGE_NAME} <<<<<<")


# Running Data Transformation Pipeline
@task(name='Data Transformation')
def data_transformation():
    STAGE_NAME = 'Data Transformation Stage'
    logger.info(f">>>>>> Stage Started : {STAGE_NAME} <<<<<<")
    data_transformation_pipeline_object = DataTransformationPipeline()
    data_transformation_pipeline_object.initiate_data_transformaiton()
    logger.info(f">>>>>> Stage Completed : {STAGE_NAME} <<<<<<")


# Running Model Training Pipeline
@task(name='Model Training')
def model_training():
    STAGE_NAME = 'Model Training Stage'
    logger.info(f">>>>>> Stage Started : {STAGE_NAME} <<<<<<")
    model_training_pipeline_object = ModelTrainingPipeline()
    model_training_pipeline_object.initiate_model_training()
    logger.info(f">>>>>> Stage Completed : {STAGE_NAME} <<<<<<")

# Running Model Evaluation Pipeline
@task(name='Model Evaluation')
def model_evaluation():
    STAGE_NAME = 'Model Evaluation Stage'
    logger.info(f">>>>>> Stage Started : {STAGE_NAME} <<<<<<")
    model_evaluation_pipeline_object = ModelEvaluationPipeline()
    model_evaluation_pipeline_object.initiate_model_evaluation()
    logger.info(f">>>>>> Stage Completed : {STAGE_NAME} <<<<<<")
    
@flow(name='wine-quality-training-piepline', log_prints=True)
def training_pipeline():
    data_ingestion()
    data_validation()
    data_transformation()
    model_training()
    model_evaluation()
    
    
if __name__ == '__main__':
    training_pipeline()