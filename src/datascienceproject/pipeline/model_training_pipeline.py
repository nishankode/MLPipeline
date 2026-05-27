# model_trainer_pipeline.py
from src.datascienceproject.config.configuration import ConfigurationManager
from src.datascienceproject.components.model_training import ModelTraining


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_training_configs()
        model_training = ModelTraining(config=model_training_config)
        model_training.train()