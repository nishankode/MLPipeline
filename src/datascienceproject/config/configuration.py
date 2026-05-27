# configuration.py
from src.datascienceproject.constants import CONFIG_FILE_PATH
from src.datascienceproject.constants import PARAMS_FILE_PATH
from src.datascienceproject.constants import SCHEMA_FILE_PATH
from src.datascienceproject.utils.common import read_yaml, create_directories

from src.datascienceproject.entity.config_entity import DataIngestionConfig
from src.datascienceproject.entity.config_entity import DataValidationConfig
from src.datascienceproject.entity.config_entity import DataTransformationConfig
from src.datascienceproject.entity.config_entity import ModelTrainingConfig
from src.datascienceproject.entity.config_entity import ModelEvaluationConfig

class ConfigurationManager:
    
	def __init__(self, 
			config_file_path = CONFIG_FILE_PATH,
			params_file_path = PARAMS_FILE_PATH,
			schema_file_path = SCHEMA_FILE_PATH
			):
		
		self.config = read_yaml(config_file_path)
		self.params = read_yaml(params_file_path)
		self.schema = read_yaml(schema_file_path)

		# creating the artifacts folder
		create_directories([self.config.artifacts_root])

	def get_data_ingestion_config(self) -> DataIngestionConfig:
		config = self.config.data_ingestion

		# creating data ingestion artifact dir
		create_directories([config.root_dir])

		data_ingestion_config = DataIngestionConfig(
			root_dir = config.root_dir,
			source_url=config.source_url,
			local_data_file = config.local_data_file,
			unzip_dir = config.unzip_dir
		)

		return data_ingestion_config

	def get_data_validation_config(self) -> DataValidationConfig:

		config = self.config.data_validation
		schema = self.schema.COLUMNS
		target = self.schema.TARGET_COLUMN

		# Creating data validation directories
		create_directories([config.root_dir])

		data_validation_config = DataValidationConfig(
			root_dir = config.root_dir,
			unzip_data_dir = config.unzip_data_dir,
			STATUS_FILE = config.STATUS_FILE,
			all_schema = schema,
			target = target
		)

		return data_validation_config
	
	def get_data_transformation_config(self) -> DataTransformationConfig:
		
		config = self.config.data_transformation
		target = self.schema.TARGET_COLUMN

		create_directories([config.root_dir])

		data_transformation_config = DataTransformationConfig(
			root_dir = config.root_dir,
			data_path = config.data_path,
			target = target.name,
			test_size = config.test_size
		)

		return data_transformation_config
	
	def get_model_training_configs(self):

		config = self.config.model_training
		params = self.params.ElasticNet
		schema = self.schema.TARGET_COLUMN

		create_directories([config.root_dir])

		model_training_configs = ModelTrainingConfig(
			root_dir = config.root_dir,
			X_train_data = config.X_train_data,
			y_train_data = config.y_train_data,
			model_name = config.model_name,
			alpha = params.alpha,
			l1_ratio = params.l1_ratio,
			target = schema.name
		)

		return model_training_configs
	
	def get_model_evaluation_configs(self):

		config = self.config.model_evaluation
		schema = self.schema
		params = self.params
		create_directories([config.root_dir])

		model_evaluation_config = ModelEvaluationConfig(
			root_dir = config.root_dir,
			X_train_data = config.X_train_data,
			X_test_data = config.X_test_data,
			y_train_data = config.y_train_data,
			y_test_data = config.y_test_data,
			model_path = config.model_path,
			metric_file_name = config.metric_file_name,
			target = schema.TARGET_COLUMN.name,
			all_params = params.ElasticNet
		)

		return model_evaluation_config