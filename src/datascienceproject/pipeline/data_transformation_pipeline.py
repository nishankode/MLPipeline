# data_transformation_pipeline.py
from src.datascienceproject.config.configuration import ConfigurationManager
from src.datascienceproject.components.data_transformation import DataTransformation

class DataTransformationPipeline:

    def __init__(self):
        pass

    def initiate_data_transformaiton(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_validation_config)
        data_transformation.train_test_split()