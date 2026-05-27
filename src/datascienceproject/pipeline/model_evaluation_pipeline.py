# model_evaluation_pipeline.py
from src.datascienceproject import logger
from src.datascienceproject.config.configuration import ConfigurationManager
from src.datascienceproject.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:

	def __init__(self):
		pass

	def initiate_model_evaluation(self):
		config = ConfigurationManager()
		model_evaluation_config = config.get_model_evaluation_configs()
		model_evaluation = ModelEvaluation(config=model_evaluation_config)
		model_evaluation.evaluate()
